# Using Scarpy splash

1. Install scrapy-splash

```bash
pip install scrapy-splash
```
2. Add the following code in your project's settings.py file:
    
```python
SPLASH_URL = 'http://localhost:8050'
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
```

## Run the spider

```bash
scrapy crawl quotes
```

## Website Scrapped: 

1. https://quotes.toscrape.com/scroll
2. https://quotes.toscrape.com/js

## Reference:

1. [ScrapeOps](https://scrapeops.io/python-scrapy-playbook/scrapy-splash/)

## Purpose

This spider was intended to learn scraping for webiste involving infinite scroll and js scripts.