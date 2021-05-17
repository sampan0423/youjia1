# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YoujiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    model_name = scrapy.Field()
    detail_price_seller = scrapy.Field()
    detail_price_fact = scrapy.Field()
    manufacturer = scrapy.Field()
    car_class = scrapy.Field()
    oil_consumption = scrapy.Field()
    displacement = scrapy.Field()
    years = scrapy.Field()
    comment_marks = scrapy.Field()
    comment_nums = scrapy.Field()
    comment_tags = scrapy.Field()
    class_content = scrapy.Field()
