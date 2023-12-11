from typing import Iterable
import scrapy
from scrapy.http import Request

from scrapy_splash_tut.items import QuoteItem
from scrapy_splash import SplashRequest

lua_script = """
function main(splash, args)
    assert(splash:go(args.url))
    
    while not splash:select('div.quote') do
        splash:wait(0.1)
        print('waiting....')
    end
    return {html=splash:htnl()}
end
"""

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # allowed_domains = ["quotes.toscrape.com"]
    # start_urls = ["https://quotes.toscrape.com"]
    '''Not Needed'''

    def start_requests(self) :
        url = 'https://quotes.toscrape.com/js'
        yield SplashRequest(
            url, 
            callback=self.parse, 
            args={'wait': 0.5, 'lua_source': lua_script , 'url': 'https://quotes.toscrape.com/scroll'}
        )

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('span small.author ::text').get()

            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item
