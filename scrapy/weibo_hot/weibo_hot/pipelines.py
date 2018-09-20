# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime


class WeiboHotPipeline(object):
    def process_item(self, item, spider):
        now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        file_name = './weibo_hot_' + now + '.txt'
        print('eldon:', file_name, item)
        with open(file_name, 'a') as fp:
            fp.write(item['hot_title'].encode('utf8') + '\n\n')
        return item
