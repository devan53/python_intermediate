# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipkartitemItem(scrapy.Item):
    prod_link = scrapy.Field()
    title = scrapy.Field()
    reviews = scrapy.Field()
    offerprice = scrapy.Field()
    initialprice = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
    images = scrapy.Field()
