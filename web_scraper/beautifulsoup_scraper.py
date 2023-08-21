```python
from bs4 import BeautifulSoup
import requests

def scrape_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return []
    except Exception as err:
        print(f'Other error occurred: {err}')
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    search_results = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and 'http' in href:
            search_results.append(href)
            if len(search_results) >= 20:
                break

    return search_results
```