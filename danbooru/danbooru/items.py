# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DanbooruItem(Item):
    image_urls = Field()
    # images = Field()
