import scrapy
import urllib.parse as urlparse
from scrapy_splash import SplashRequest
from tutorial.items import FitItem, FitTypeItem


class FitSpider(scrapy.Spider):
    name = 'fit'
    # allowed_domains = ['hiyd.com']
    start_urls = ['https://hiyd.com/dongzuo/']

    def __init__(self):
        self.base_url = 'https://hiyd.com'

    def parse(self, response):
        params = {
            'equipment',
            'muscle',
            'difficulty'
        }

        for i in response.xpath('//a[@class="sort-item"]'):
            parsed = urlparse.urlparse(i.xpath('@href').extract_first())
            querys = urlparse.parse_qs(parsed.query)

            for q in querys:
                if q in params:
                    item = FitTypeItem()
                    item['value'] = querys[q][0]
                    item['name'] = i.xpath('text()').extract_first()
                    item['type'] = q
                    yield item

            yield scrapy.Request(i.xpath('@href').extract_first(), callback=self.parsePage)

    def parsePage(self, response):
        pages = response.xpath('//div[@class="mod-page"]/a/@href').extract()

        if len(pages) > 0:
            for i in pages:
                url = urlparse.urljoin(response.url, i)
                yield scrapy.Request(url, callback=self.parseList)
        else:
            yield scrapy.Request(response.url, callback=self.parseList, dont_filter=True)

    def parseList(self, response):
        for i in response.xpath('//li[@class="hvr-glow"]'):
            for sex in [1, 2]:
                tags = i.xpath('.//div[@class="tag"]/span/text()').extract()
                params = {
                    'sex': sex,
                    'name': i.xpath('.//span[@class="title"]/text()').extract_first(),
                    'level': tags[0] if tags[0] else None,
                    'position': tags[2] if tags[2] else None,
                    'apparatus': tags[1] if tags[1] else None
                }

                url = urlparse.urljoin(self.base_url, i.xpath('a/@href').extract_first())
                yield SplashRequest(url, endpoint='execute', args={'lua_source': """
                function main(splash, args)
                    splash:add_cookie{"coach_gender", "%s", "/", domain=".hiyd.com"}
                    splash.html5_media_enabled = true
                    assert(splash:go(args.url))
                    assert(splash:wait(2))
                    return {
                        html = splash:html(),
                        png = splash:png(),
                        har = splash:har(),
                    }
                end
                """ % sex}, callback=lambda response, params=params: self.parseItem(response, params))

    def parseItem(self, response, params):
        try:
            item = FitItem()
            for i in params:
                item[i] = params[i]
            item['cover'] = response.xpath('//div[@class="video-poster"]//img/@src').extract_first()
            item['video'] = response.xpath('//video/@src').extract_first()
            item['essentials'] = response.xpath('//ul[@class="guide-pic-list clearfix"]//img/@src').extract()
            item['sketch_map'] = response.xpath('//div[@class="guide-pic"]/img/@src').extract()
            item['explain'] = response.xpath('//div[@class="guide-text"]').extract_first()
            yield item
        except Exception as e:
            print(e)
            yield scrapy.Request(
                response.url,
                callback=lambda response, params=params: self.parseItem(response, params),
                dont_filter=True
            )
