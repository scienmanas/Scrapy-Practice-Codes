from typing import Iterable
import scrapy
from scrapy.http import Request

from scrapy_splash_tut.items import QuoteItem
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # allowed_domains = ["quotes.toscrape.com"]
    # start_urls = ["https://quotes.toscrape.com"]
    '''Not Needed'''

    def start_requests(self) :
        url = 'https://quotes.toscrape.com'
        yield SplashRequest(url, callback=self.parse)

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('span small.author ::text').get()

            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
