```python
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .scrapy_spider import MySpider
from .beautifulsoup_scraper import scrape_data as bs_scrape_data
from .openai_api import summarize_text
from .pdf_generator import generate_pdf

def main():
    search_url = sys.argv[1]
    process = CrawlerProcess(get_project_settings())
    process.crawl(MySpider, start_urls=[search_url])
    process.start()  # the script will block here until the crawling is finished

    # If Scrapy fails to scrape data, use BeautifulSoup as a backup
    if not MySpider.data:
        MySpider.data = bs_scrape_data(search_url)

    # Summarize the scraped data
    summarized_text = summarize_text(MySpider.data)

    # Generate a PDF from the summarized text
    generate_pdf(summarized_text)

if __name__ == "__main__":
    main()
```