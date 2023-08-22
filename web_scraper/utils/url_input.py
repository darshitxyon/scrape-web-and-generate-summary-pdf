```python
import argparse

def get_search_url():
    parser = argparse.ArgumentParser(description='Web Scraper')
    parser.add_argument('url', help='Search URL to scrape')
    args = parser.parse_args()
    return args.url
```