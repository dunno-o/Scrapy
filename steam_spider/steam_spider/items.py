# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    release_date = scrapy.Field()
    tags = scrapy.Field()
    developer = scrapy.Field()
    categories = scrapy.Field()
    reviews_count = scrapy.Field()
    mark = scrapy.Field()
    platforms = scrapy.Field()