# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import logging

class MansetPipeline(object):

    picked_domains = [ 'i.hurimg.com' ]

    def process_item(self, item, spider):
        url = item.get('url', None)
        if None is url:
            raise DropItem("Is not Manset item")

        for domain in self.picked_domains:
            if domain in unicode(url).lower():
                return item

        raise DropItem("Is not in picked domains")



