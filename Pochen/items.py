# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PochenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    homepage = scrapy.Field()
    h1 = scrapy.Field()
    text = scrapy.Field()
    span = scrapy.Field()
    tags = scrapy.Field()
    page = scrapy.Field()
