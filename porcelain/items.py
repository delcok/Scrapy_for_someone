# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PorcelainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    proceleain_name = scrapy.Field()
    proceleain_Appraisal = scrapy.Field()
    proceleain_final_price = scrapy.Field()


class jiadeItems(scrapy.Item):
    num = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()

