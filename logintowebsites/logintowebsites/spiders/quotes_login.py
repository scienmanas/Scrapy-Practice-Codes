from typing import Iterable
import scrapy
from scrapy.http import Request
from scrapy.http import FormRequest

class QuotesLoginSpider(scrapy.Spider):
    name = "quotes_login"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/login"]

    def start_requests(self):
        login_url = "https://quotes.toscrape.com/login"
        yield scrapy.Request(login_url, callback=self.login)

    def login(self, response):
        token = response.css(
            'form input[name=csrf_token]::attr(value)').extract_first()
        yield FormRequest.from_response(response, formdata= {
            'csrf_token': token,
            'password': 'foobar',
            'username': 'user'
            },
            callback=self.start_scrapping)

    def start_scrapping(self, response) :
        for quote in response.css('div.quote') :
            yield {
                'text' : quote.css('span.text::text').get(),
                'author' : quote.css('small.author ::text').get(),
                'tags' : quote.css('div.tags a.tag::text').getall(),
            }

    # def parse(self, response):
    #     pass
