from typing import Iterable
import scrapy
from scrapy.http import Request


class AmazonLoginTokensSpider(scrapy.Spider):
    name = "amazon_login_tokens"
    allowed_domains = ["www.amazom.com"]
    start_urls = ["https://www.amazom.com"]

    def start_requests(self) :
        url = "https://www.amazom.com"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass

## Very difficult to do since the headers are dynamic and continously changing
