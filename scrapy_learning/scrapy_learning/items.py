# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLearningItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    serial_number = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    evaluate = scrapy.Field()
    describe = scrapy.Field()



