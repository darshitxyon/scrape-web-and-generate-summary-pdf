# Web Scraper

This is a web scraping tool built to extract data from any search engine.

## Tech Stack

- Python with Scrapy and BeautifulSoup for web scraping

## Features

- Extract all search result links from search engine search page.
- Handle pagination (up to 20 links max) and dynamic content
- Extract text/paragraph data from those links on search engine and summarise it using OpenAI's API (using model 'gpt-3.5-turbo')
- Summary up to 500 words max is created and then populated along with the link in a PDF.
- Each link along with the summary of information in that page is populated in each page.
- Single search Engine link should generate a single PDF with each page pertaining to each link on the search and the summary of data in that link.
- Pass the search url as input prompted to user.

## How to Run

1. Install the required packages from `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```

2. Run the main script and pass the search URL as an argument:

```bash
python web_scraper/main.py --url "your_search_url"
```

Replace `"your_search_url"` with the URL of the search engine page you want to scrape.

## Files

- `web_scraper/main.py`: The main script that runs the web scraper.
- `web_scraper/scraping/scrapy_spider.py`: The Scrapy spider for web scraping.
- `web_scraper/scraping/beautifulsoup_scraper.py`: The BeautifulSoup scraper for web scraping.
- `web_scraper/summary/openai_api.py`: The script that uses OpenAI's API to summarise the scraped data.
- `web_scraper/pdf_generation/pdf_generator.py`: The script that generates a PDF from the summarised data.
- `web_scraper/utils/url_input.py`: The script that prompts the user for the search URL.
- `requirements.txt`: The file containing the required Python packages.
- `README.md`: This file, containing the description and instructions for this project.