# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ps4GameItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    price = scrapy.Field()
    star = scrapy.Field()
    n_sale = scrapy.Field()
    year = scrapy.Field()
    plat = scrapy.Field()
    pass
