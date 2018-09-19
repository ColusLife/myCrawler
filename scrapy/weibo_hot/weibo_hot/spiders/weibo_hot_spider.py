# -*- coding: utf-8 -*-
import scrapy
from weibo_hot.items import WeiboHotItem


class WeiboHotSpider(scrapy.Spider):
    name = 'weibo_hot_spider'
    allowed_domains = ['weibo.com']
    start_urls = ['https://weibo.com/a/hot/realtime']

    def parse(self, response):
        selector = response.xpath('//div[@class="list_title_b"]')
        items = []
        for sub_selector in selector:
            item = WeiboHotItem()
            item['hot_name'] = sub_selector.xpath('./a/text()').extract()
            items.append(item)
        return items
