from typing import Iterable
import scrapy
from scrapy.http import Request
from scrapy_playwright_tut.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/js/"]

    def start_requests(self) :
        url = "https://quotes.toscrape.com/js/"
        yield scrapy.Request(url=url, meta={'playwright': True})

    def parse(self, response):
        quote_item = QuoteItem()

        for quote in response.css('div.quote') :
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item


