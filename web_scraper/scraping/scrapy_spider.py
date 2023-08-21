```python
import scrapy

class SearchEngineSpider(scrapy.Spider):
    name = 'search_engine_spider'

    def __init__(self, search_url='', *args, **kwargs):
        super(SearchEngineSpider, self).__init__(*args, **kwargs)
        self.start_urls = [search_url]

    def parse(self, response):
        links = response.css('a::attr(href)').getall()
        links = [link for link in links if 'http' in link][:20]  # Limit to 20 links

        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_link)

    def parse_link(self, response):
        data = {}
        data['url'] = response.url
        data['title'] = response.css('title::text').get()
        data['text'] = ' '.join(response.css('p::text').getall())  # Extract paragraph data
        yield data
```