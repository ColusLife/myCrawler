# -*- coding: utf-8 -*-
import scrapy


class HzMovieSpider(scrapy.Spider):
    name = 'hz_movie'
    allowed_domains = ['jycinema.com']
    start_urls = ['http://jycinema.com/']

    def parse(self, response):
        pass
