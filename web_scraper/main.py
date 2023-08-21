```python
import sys
from scraping.scrapy_spider import ScrapySpider
from scraping.beautifulsoup_scraper import BeautifulSoupScraper
from summary.openai_api import OpenAISummarizer
from pdf_generation.pdf_generator import PDFGenerator
from utils.url_input import get_search_url

def main():
    # Get the search URL from command line argument
    search_url = get_search_url(sys.argv)

    # Initialize the Scrapy spider
    scrapy_spider = ScrapySpider(search_url)

    # Extract links using Scrapy
    links = scrapy_spider.extract_links()

    # If Scrapy fails, use BeautifulSoup as a backup
    if not links:
        bs_scraper = BeautifulSoupScraper(search_url)
        links = bs_scraper.extract_links()

    # Initialize the OpenAI summarizer
    summarizer = OpenAISummarizer()

    # Initialize the PDF generator
    pdf_generator = PDFGenerator()

    # For each link, extract the text, summarize it, and add it to the PDF
    for link in links:
        text = scrapy_spider.extract_text(link) or bs_scraper.extract_text(link)
        summary = summarizer.summarize(text)
        pdf_generator.add_page(link, summary)

    # Save the PDF
    pdf_generator.save_pdf()

if __name__ == "__main__":
    main()
```