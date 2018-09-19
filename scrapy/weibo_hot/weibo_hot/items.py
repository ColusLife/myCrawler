# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboHotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hot_name = scrapy.Field() # hot name
