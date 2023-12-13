from typing import Iterable
import scrapy
from scrapy.http import Request
from scrapy_playwright_tut.items import QuoteItem
from scrapy_playwright.page import PageMethod


class QuotesSpider(scrapy.Spider):

    # name = "proxy"
    # custom_settings = {
    #     "PLAYWRIGHT_LAUNCH_OPTIONS": {
    #         "proxy": {
    #             "server": "http://myproxy.com:3128"
    #             "username": "user",
    #             "password": "pass",
    #         },
    #     }
    # }
    
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/scroll"]

    def start_requests(self) :
        url = "https://quotes.toscrape.com/scroll"
        yield scrapy.Request(url=url, meta=dict(
            playwright = True,
            playwright_include_page = True,
            playwright_page_methods = [
                PageMethod('wait_for_selector', 'div.quote'),
                PageMethod('wait_for_selector', 'div.tags'),
                PageMethod('evaluate','window.scrollBy(0, document.body.scrollHeight)'),
                PageMethod('wait_for_selector', 'div.quote:nth-child(11)')
                ],
                errback=self.errback,
            ))

    async def parse(self, response):
        page = response.meta["playwright_page"]

        # Take Screenshot 
        # Hats off to this function
        screenshot = await page.screenshot(path='ss_page.png', full_page=True)

        await page.close()
        quote_item = QuoteItem()
        for quote in response.css('div.quote') :
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item
    
    async def errback(self, failure) :
        page = failure.request.meta["playwright_page"]
        await page.close()

