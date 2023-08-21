```python
import sys
from scraping.scrapy_spider import ScrapySpider
from scraping.beautifulsoup_scraper import BeautifulSoupScraper
from summary.openai_api import OpenAIAPI
from pdf_generation.pdf_generator import PDFGenerator

def main():
    # Get the search URL from command line arguments
    search_url = sys.argv[1]

    # Initialize the Scrapy spider
    spider = ScrapySpider(search_url)

    # Scrape the search results
    try:
        search_results = spider.scrape()
    except Exception as e:
        print(f"Scrapy failed with error: {e}")
        print("Switching to BeautifulSoup for scraping...")
        bs_scraper = BeautifulSoupScraper(search_url)
        search_results = bs_scraper.scrape()

    # Initialize the OpenAI API
    openai_api = OpenAIAPI()

    # Summarize the search results
    summarized_results = openai_api.summarize(search_results)

    # Initialize the PDF generator
    pdf_generator = PDFGenerator()

    # Generate the PDF
    pdf_generator.generate(summarized_results)

if __name__ == "__main__":
    main()
```