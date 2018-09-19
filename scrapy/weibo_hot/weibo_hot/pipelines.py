# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime


class WeiboHotPipeline(object):
    def process_item(self, item, spider):
        now = datetime.strftime('%Y-%m-%d %H:%M:%S', datetime.now)
        file_name = 'weibo_hot_' + now + '.txt'
        with open(file_name, 'a') as fp:
            fp.write(item['weibo_hot'][0].encode('utf8') + '\n\n')
        return item
