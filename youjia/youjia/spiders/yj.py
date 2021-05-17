# -*- coding: utf-8 -*-
import scrapy


class YjSpider(scrapy.Spider):
    name = 'yj'
    allowed_domains = ['youjia.baidu.com']
    start_urls = ['https://youjia.baidu.com/view/carDatabase?title=%E7%8E%B0%E4%BB%A3&key=code&val=174&sa=pc_growth_1']

    def parse(self, response):
        # print(response.css('div.car-info a::attr(href)'))  #only 24 selectors
        print(len(response.css('p.car-name::text').getall()))
        # print(response.xpath('//*[@id="app"]/section/main/div/section/div[2]/div[2]/div[6]/a/p[1]/text').get())