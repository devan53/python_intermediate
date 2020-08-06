# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonitemItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    prod_link = scrapy.Field()
    title = scrapy.Field()
    reviews = scrapy.Field()
    offerprice = scrapy.Field()
    initialprice = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
    image1 = scrapy.Field()
    # image2 = scrapy.Field()
    # image3 = scrapy.Field()
    # image4 = scrapy.Field()
    # aaa = scrapy.Field()
