import scrapy
from bs4 import BeautifulSoup
import requests

class SteamSpiderSpider(scrapy.Spider):
    name = 'steam_spider'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?term=инди&supportedlang=russian&ndl=1',
                  'https://store.steampowered.com/search/?term=action&supportedlang=russian&ndl=1',
                  'https://store.steampowered.com/search/?term=adventure&supportedlang=russian&ndl=1']


    def start_requests(self):
        for req in ['indie', 'action', 'adventure']:
            for page in range(1, 3):
                url = 'https://store.steampowered.com/search/?term={}&page={}'.format(req, page)
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for link in response.xpath('//a[contains(@href, "app")]/@href').extract():
            yield response.follow(link, callback=self.parse_game)


    def parse_game(self, response):
        platforms = set()

        for platform in response.css('div').xpath('@data-os'):
            platforms.add(platform.get().strip())

        yield {
            'name': response.xpath('//span[@itemprop="name"]/text()').extract(),
            'categories': response.xpath('//div[@class="blockbg"]/a/text()').extract(),
            'reviews_count': response.xpath('//meta[@itemprop="reviewCount"]/@content').extract(),
            'mark': response.xpath('//meta[@itemprop="reviewCount"]/@content').extract(),
            'release_date': response.xpath('//div[@class="date"]/text()').extract(),
            'developer' : response.xpath('//div[@class="dev_row"]/a/text()').extract(),
            'tags': [el.split('\t\t\t\t\t\t\t\t\t\t\t\t')[1] for el in response.xpath('//a[@class="app_tag"]/text()').extract()],
            'price': response.xpath('//div[@class="discount_final_price"]/text()').extract(),
            'platforms': list(platforms)
        }

