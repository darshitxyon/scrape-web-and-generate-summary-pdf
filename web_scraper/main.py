```python
import config
from scrapy_spider import ScrapySpider
from beautifulsoup_scraper import BeautifulSoupScraper
from openai_api import OpenAIAPI
from pdf_generator import PDFGenerator

class Main:
    def __init__(self):
        self.scrapy_spider = ScrapySpider()
        self.bs_scraper = BeautifulSoupScraper()
        self.openai_api = OpenAIAPI()
        self.pdf_generator = PDFGenerator()

    def run(self, search_url):
        # Scrape links using Scrapy
        links = self.scrapy_spider.scrape_links(search_url)

        # If Scrapy fails, use BeautifulSoup as a backup
        if not links:
            links = self.bs_scraper.scrape_links(search_url)

        # Limit to 20 links
        links = links[:config.MAX_LINKS]

        for link in links:
            # Scrape text data from each link
            text_data = self.scrapy_spider.scrape_text(link)

            # If Scrapy fails, use BeautifulSoup as a backup
            if not text_data:
                text_data = self.bs_scraper.scrape_text(link)

            # Summarize the text data using OpenAI's API
            summary = self.openai_api.summarize_text(text_data)

            # Generate a PDF page for the link and its summary
            self.pdf_generator.generate_pdf(link, summary)

        # Save the PDF
        self.pdf_generator.save_pdf()

if __name__ == "__main__":
    main = Main()
    main.run(config.SEARCH_URL)
```