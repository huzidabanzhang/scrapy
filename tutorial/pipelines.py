# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TutorialPipeline:
    def process_item(self, item, spider):
        return item


class FitPipeline:
    def process_item(self, item, spider):
        # print(item)
        return item


class FitTypePipeline:
    def process_item(self, item, spider):
        # print(item)
        return item


class KeepSelectorPipeline:
    def process_item(self, item, spider):
        # print(item)
        return item


class KeepSelectorOptionsPipeline:
    def process_item(self, item, spider):
        # print(item)
        return item


class KeepSortPipeline:
    def process_item(self, item, spider):
        # print(item)
        return item


class KeepPipeline:
    def process_item(self, item, spider):
        # print(item)
        return item
