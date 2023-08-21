```python
from bs4 import BeautifulSoup
import requests
from config import MAX_LINKS

def scrape_links_with_bs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('a')
    links = [link.get('href') for link in search_results]
    return links[:MAX_LINKS]

def scrape_text_with_bs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([p.text for p in paragraphs])
    return text
```