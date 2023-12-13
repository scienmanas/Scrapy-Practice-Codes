# import scrapy
from pagination.items import BlogItem
from scrapy.spiders import SitemapSpider


class PaginationSitemapSpider(SitemapSpider):
    name = "pagination_sitemap"
    # allowed_domains = ["www.scraperapi.com"]
    # start_urls = ["https://www.scraperapi.com/"]
    sitemap_urls = ['https://www.scraperapi.com/post-sitemap.xml']
    sitemap_rules = [
        ('blog/', 'parse'),
    ]


    def parse(self, response):
        blog_items = BlogItem()
        blog_items['url'] = response.url
        blog_items['title'] = response.css('h1.elementor-heading-title ::text').get()
        yield blog_items

