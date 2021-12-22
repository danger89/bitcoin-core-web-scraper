# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.files import FilesPipeline
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

# Template:
#class BitcoinscraperPipeline:
#    def process_item(self, item, spider):
#       return item

# Inherent from the built-in FilesPipeline class
class BitcoinscraperFilesPipeline(FilesPipeline):
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('file_urls'):
            return super().process_item(item, spider)
        else:
            raise DropItem(f"Not a download item, missing file_urls field.")

    def file_path(self, request, response=None, info=None):
        folder_name: str = request.url.split("/")[-2]
        file_name: str = request.url.split("/")[-1]
        return f'{folder_name}/{file_name}'
