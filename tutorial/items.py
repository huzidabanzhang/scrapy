# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FitItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()  # 级别
    position = scrapy.Field()  # 部位
    apparatus = scrapy.Field()  # 器械
    sex = scrapy.Field()
    cover = scrapy.Field()  # 封面
    video = scrapy.Field()
    essentials = scrapy.Field()  # 要领
    sketch_map = scrapy.Field()  # 示意图
    explain = scrapy.Field()  # 说明


class FitTypeItem(scrapy.Item):
    name = scrapy.Field()
    value = scrapy.Field()
    type = scrapy.Field()


class KeepSelectorItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    value = scrapy.Field()


class KeepSelectorOptionsItem(scrapy.Item):
    id = scrapy.Field()
    parent_id = scrapy.Field()
    name = scrapy.Field()
    value = scrapy.Field()


class KeepSortItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    value = scrapy.Field()


class KeepItem(scrapy.Item):
    pass
