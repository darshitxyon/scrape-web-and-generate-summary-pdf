```python
from bs4 import BeautifulSoup
import requests

def beautifulsoup_scraper(search_url):
    # Initialize a session
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})

    # Send a GET request
    response = session.get(search_url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links on the page
    links = soup.find_all('a')

    # Extract href attribute from each link and store
    search_result_links = [link.get('href') for link in links]

    # Limit to 20 links
    search_result_links = search_result_links[:20]

    # Extract text/paragraph data from those links
    link_data = []
    for link in search_result_links:
        try:
            link_response = session.get(link)
            link_soup = BeautifulSoup(link_response.content, 'html.parser')
            paragraphs = link_soup.find_all('p')
            text_data = ' '.join([p.text for p in paragraphs])
            link_data.append((link, text_data))
        except Exception as e:
            print(f"Error occurred while processing link {link}: {e}")

    return link_data
```