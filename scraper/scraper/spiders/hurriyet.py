# -*- coding: utf-8 -*-
import scrapy
from scraper.items import Manset

class HurriyetSpider(scrapy.Spider):
    name = "hurriyet"
    allowed_domains = ["hurriyet.com.tr"]
    start_urls = (
        'http://www.hurriyet.com.tr/',
    )

    def parse(self, response):
        for src in response.css('img::attr(src)'):
            yield Manset({'url' : src.extract() })