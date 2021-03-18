# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exceptions import DropItem


import json


class DoubanPipeline(object):

    def open_spider(self, spider):
        self.file = open('resultself.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # Remove invalid data
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing %s of blogpost from %s" % (data, item['url']))
        if valid:
            # Insert data into database
            new_moive = [{
                "name": item['name'][0],
                "year": item['year'][0],
                "score": item['score'],
                "director": item['director'],
                "classification": item['classification'],
                "actor": item['actor']
            }]
            line = json.dumps(new_moive) + "\n"
            self.file.write(line)
        return item

