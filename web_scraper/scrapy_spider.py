```python
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SearchEngineSpider(CrawlSpider):
    name = "search_engine_spider"

    def __init__(self, search_url='', *args, **kwargs):
        super(SearchEngineSpider, self).__init__(*args, **kwargs)
        self.start_urls = [search_url]
        self.rules = (
            Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="next"]',)), callback="parse_item", follow= True),
        )

    def parse_item(self, response):
        page_links = response.css('a::attr(href)').getall()
        page_text = response.css('p::text').getall()
        yield {
            'links': page_links[:20],
            'text': page_text
        }

def scrape_data(search_url):
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'result.json'
    })

    process.crawl(SearchEngineSpider, search_url=search_url)
    process.start()
```
