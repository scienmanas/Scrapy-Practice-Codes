# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapySplashTutPipeline:

    def process_item(self, item, spider):
        return item

class CleanTheDataPipeline :

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Tags
        tags_list = adapter.get("tags")
        for i in range(0,len(tags_list)) :
            tags_list[i] = tags_list[i].replace('"','')
            tags_list[i] = tags_list[i].replace("'",'')

        adapter["tags"] = tags_list

        # Quotes Text
        replace_items = ['"', '“','”']
        text = adapter.get("text")
        for replacable_item in replace_items :
            text = text.replace(replacable_item,'')
        adapter['text'] = str(text)

        return item