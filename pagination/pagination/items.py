# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaginationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BlogItem(scrapy.Item) :

    url = scrapy.Field()
    title = scrapy.Field()

class QuoteItem(scrapy.Item) :

    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class CharacterItem(scrapy.Item) :

    name = scrapy.Field()
    status = scrapy.Field()
    species = scrapy.Field()