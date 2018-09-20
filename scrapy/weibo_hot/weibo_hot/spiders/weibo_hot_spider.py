# -*- coding: utf-8 -*-
import scrapy
from weibo_hot.items import WeiboHotItem


class WeiboHotSpider(scrapy.Spider):
    name = 'weibo_hot_spider'
    allowed_domains = ['weibo.com']
    start_urls = ['https://weibo.com/login.php']

    def parse(self, response):
        selector = response.xpath('//div[@class="footer_link clearfix"]')
        items = []
        for sub_selector in selector:
            dt_selector = sub_selector.xpath('./dl/dt/text()')
            for dt_s in dt_selector:
                item = WeiboHotItem()
                item['hot_title'] = dt_s.extract()
                items.append(item)
                print(item)
        return items
