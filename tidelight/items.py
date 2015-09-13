# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TideLightItem(scrapy.Item):
    low_1 = scrapy.Field()
    high_1 = scrapy.Field()
    low_2 = scrapy.Field()
    high_2 = scrapy.Field()
    pass
