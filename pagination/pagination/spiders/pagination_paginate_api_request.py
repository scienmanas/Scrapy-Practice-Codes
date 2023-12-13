import scrapy
from pagination.items import CharacterItem

class PaginationPaginateApiRequestSpider(scrapy.Spider):
    name = "pagination_paginate_api_request"
    allowed_domains = ["rickandmortyapi.com"]
    start_urls = ["https://rickandmortyapi.com/api/character/"]

    def parse(self, response):
        json_response = response.json()
        character_item = CharacterItem()
        for character in json_response.get('results',[]) :
            character_item['name'] = character.get('name')
            character_item['status'] = character.get('status')
            character_item['species'] = character.get('species')
            yield character_item

        next_page = json_response['info'].get('next')
        if next_page :
            yield response.follow(next_page, callback= self.parse)


## Check Api for more clarification 