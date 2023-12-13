import scrapy
import autopager
import requests
# Autopager is a Python package that detects and classifies pagination links on a page, using a pre-trained machine learning model. 

class AutopagerPaginationSpider(scrapy.Spider):
    name = "autopager_pagination"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        url = "http://quotes.toscrape.com"
        yield {
            'links': autopager.urls(requests.get(url)),
        }
