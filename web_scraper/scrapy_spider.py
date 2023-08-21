```python
import scrapy
from scrapy.http import Request
from config import MAX_LINKS

class SearchEngineSpider(scrapy.Spider):
    name = 'search_engine_spider'
    allowed_domains = ['searchengine.com']
    start_urls = ['http://searchengine.com/']

    def parse(self, response):
        links = response.css('a::attr(href)').getall()
        for link in links[:MAX_LINKS]:
            yield Request(url=link, callback=self.parse_link)

    def parse_link(self, response):
        link = response.url
        text_data = response.css('p::text').getall()
        yield {'link': link, 'text_data': text_data}
```
This is a basic Scrapy spider that starts at a given search engine's homepage, extracts all the links on the page, and then visits each link to extract the text data. The number of links visited is limited by the `MAX_LINKS` configuration. The extracted data is yielded as a dictionary with the link and the text data. The actual domain and start URL would need to be replaced with the actual search engine's domain and URL.