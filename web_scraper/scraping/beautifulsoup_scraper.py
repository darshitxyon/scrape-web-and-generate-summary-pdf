```python
from bs4 import BeautifulSoup
import requests

def get_links(search_url):
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url and 'http' in url:
            links.append(url)
    
    return links[:20]

def get_page_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')
    page_data = ' '.join([p.text for p in paragraphs])

    return page_data
```