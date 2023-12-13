import scrapy


class AutopagerPaginationSpider(scrapy.Spider):
    name = "autopager_pagination"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        pass
