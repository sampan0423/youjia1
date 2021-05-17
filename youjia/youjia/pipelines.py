# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class YoujiaPipeline(object):

    def __init__(self):
        self.csvf = open('data.csv','a+',encoding='utf-8',newline='')
        self.writer = csv.writer(self.csvf)
        self.writer.writerow(('model_name','detail_price_fact','car_class','displacement'))

        self.csvf.close()

    def process_item(self, item, spider):
        with open('data.csv','a+',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow((item['model_name'],item['detail_price_fact'],item['car_class'],item['displacement']))
        return item
