# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnnSpItem(scrapy.Item):
    Ticker = scrapy.Field()
    Company = scrapy.Field()
    NetIncome = scrapy.Field()
    Sector = scrapy.Field()
    Industry = scrapy.Field()
    TotalAssets  = scrapy.Field()
    TotalShareholderEquity  = scrapy.Field()

