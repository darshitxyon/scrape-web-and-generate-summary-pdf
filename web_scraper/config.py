```python
# Configuration file for the web scraper

# OpenAI API key
OPENAI_API_KEY = "your_openai_api_key"

# Maximum number of links to scrape
MAX_LINKS = 20

# Maximum summary length
MAX_SUMMARY_LENGTH = 500

# Scrapy settings
SCRAPIE_SETTINGS = {
    'BOT_NAME': 'web_scraper',
    'SPIDER_MODULES': ['web_scraper.spiders'],
    'NEWSPIDER_MODULE': 'web_scraper.spiders',
    'ROBOTSTXT_OBEY': True,
}

# BeautifulSoup settings
BEAUTIFULSOUP_SETTINGS = {
    'features': 'html.parser'
}

# OpenAI settings
OPENAI_SETTINGS = {
    'engine': 'gpt-3.5-turbo',
    'temperature': 0.5,
    'max_tokens': MAX_SUMMARY_LENGTH
}

# PDF settings
PDF_SETTINGS = {
    'page_size': 'A4',
    'margin': 1
}
```