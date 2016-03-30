# -*- coding: utf-8 -*-
import scrapy
from scraper.items import Manset
from urlparse import urljoin

import  logging

class HurriyetSpider(scrapy.Spider):
    name = "hurriyet"
    allowed_domains = ["hurriyet.com.tr"]
    start_urls = (
        'http://www.hurriyet.com.tr/',
    )

    def parse(self, response):
        for img in response.css('img'):
            src_sel = img.xpath('@src')

            if not len(src_sel):
                continue

            manset = Manset()
            manset['url'] = src_sel[0].extract()


            a_sel = img.xpath('parent::a/@href')
            if not len(a_sel):
                yield  manset
                continue

            manset['href'] = urljoin(response.url, a_sel[0].extract())
            yield manset
