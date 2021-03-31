import scrapy
import json
import uuid
from tutorial.items import KeepSelectorItem, KeepSelectorOptionsItem, KeepSortItem, KeepItem


class KeepSpider(scrapy.Spider):
    name = 'keep'
    # allowed_domains = ['api.gotokeep.com']
    # start_urls = ['https://api.gotokeep.com/course/v1/discover?category=yoga&courseRank=1']

    headers = {
        'Authorization': ''
    }

    def get_uuid(self):
        return str(uuid.uuid1())

    def start_requests(self):
        url = 'https://api.gotokeep.com/course/v1/discover?category=yoga&courseRank=1'
        yield scrapy.Request(url, method='GET', callback=self.parse_type, headers=self.headers)

    def parse_type(self, response):
        data = json.loads(response.text)

        if data['ok']:
            selector = data['data']['selector']

            for i in selector['sortTypes']:
                item = KeepSortItem()
                item['id'] = self.get_uuid()
                item['name'] = i['name']
                item['value'] = i['id']
                yield item

            for i in selector['items']:
                item = KeepSelectorItem()
                item['id'] = self.get_uuid()
                item['name'] = i['name']
                item['value'] = i['id']
                yield item

                for option in i['options']:
                    o = KeepSelectorOptionsItem()
                    o['id'] = self.get_uuid()
                    o['parent_id'] = item['id']
                    o['name'] = option['displayName']
                    o['value'] = option['labelId']
                    yield o

        headers = self.headers
        headers['Content-Type'] = 'application/json'

        yield scrapy.Request(
            'https://api.gotokeep.com/course/v1/selector',
            method='POST',
            callback=self.parse_list,
            body=json.dumps({
                "size": "20",
                "selectors": {},
                "category": "yoga",
                "lastId": "",
                "sortType": "default"
            }),
            headers=headers
        )

    def parse_list(self, response):
        data = json.loads(response.text)

        if data['ok']:
            datas = data['data']['datas']
            for i in datas:
                item = KeepItem()
                for o in i:
                    item.fields[o] = scrapy.Field()
                    item[o] = i[o]
                yield item

            if data['data']['lastPage'] == False:
                yield scrapy.Request(
                    'https://api.gotokeep.com/course/v1/selector',
                    method='POST',
                    callback=self.parse_list,
                    body=json.dumps({
                        "size": "20",
                        "selectors": {},
                        "category": "yoga",
                        "lastId": data['data']['lastId'],
                        "sortType": "default"
                    }),
                    headers=headers
                )
