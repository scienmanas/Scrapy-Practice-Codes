from typing import Iterable
import scrapy
from scrapy.http import Request
import base64
from scrapy_splash_tut.items import QuoteItem
from scrapy_splash import SplashRequest

# javascript_script = """
# element = document.querySelector('h1').innerHTML = 'The best quotes of all time!'
# """

# # Script for mouse clicking
# lua_script = """
# function main(splash,args)
#     assert(splash:go(args.url))

#     local element = splash:select('body > div > nav > ul > li > a')
#     element:mouse_click()
    
#     splash:wait(splash.args.wait)  
#     return splash:html()
# end
# """

lua_script = """
function main(splash)
    local num_scrolls = 10
    local scroll_delay = 1.0

    local scroll_to = splash:jsfunc("window.scrollTo")
    local get_body_height = splash:jsfunc(
        "function() {return document.body.scrollHeight;}"
    )
    assert(splash:go(splash.args.url))
    splash:wait(splash.args.wait)

    for _ = 1, num_scrolls do
        scroll_to(0, get_body_height())
        splash:wait(scroll_delay)
    end        
    return splash:html()
end
"""

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # allowed_domains = ["quotes.toscrape.com"]
    # start_urls = ["https://quotes.toscrape.com"]
    '''Not Needed'''

    def start_requests(self) :
        url = 'https://quotes.toscrape.com/scroll'
        yield SplashRequest(
            url, 
            callback=self.parse, 
            endpoint= 'execute',
        #    args={
        #         'wait': 2,
        #         'js_source': javascript_script, 
        #         'html': 1, 
        #         'png': 1, 
        #         'width': 1000,
        #     }
            args={'wait': 0.5, 'lua_source': lua_script ,  'url': 'https://quotes.toscrape.com/scroll'}
        )

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('span small.author ::text').get()

            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()

            ## For Screenshot
            # imgdata = base64.b64decode(response.data['png'])
            # file_name = 'screenshot_website.png'
            # with open(file_name,'wb') as f :
            #     f.write(imgdata)
            yield quote_item
