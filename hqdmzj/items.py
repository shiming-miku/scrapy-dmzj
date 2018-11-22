# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HqdmzjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    time = scrapy.Field()
    title = scrapy.Field()
    cover = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()


class ContentItem(scrapy.Item):
    text = scrapy.Field()
    url = scrapy.Field()
