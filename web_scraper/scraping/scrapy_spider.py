```python
import scrapy

class SearchEngineSpider(scrapy.Spider):
    name = 'search_engine_spider'
    allowed_domains = ['searchengine.com']  # Replace with actual search engine domain
    start_urls = ['http://searchengine.com/']  # Replace with actual search engine URL

    def __init__(self, search_url=None, *args, **kwargs):
        super(SearchEngineSpider, self).__init__(*args, **kwargs)
        self.start_urls = [search_url]

    def parse(self, response):
        links = response.css('a::attr(href)').getall()  # Replace with actual CSS selector for links
        links = links[:20]  # Limit to 20 links

        for link in links:
            yield scrapy.Request(response.urljoin(link), callback=self.parse_link)

    def parse_link(self, response):
        text_data = response.css('p::text').getall()  # Replace with actual CSS selector for text/paragraph data
        yield {
            'link': response.url,
            'text_data': text_data
        }
```