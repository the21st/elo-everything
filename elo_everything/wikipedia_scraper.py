```python
import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(concept):
    url = f"https://en.wikipedia.org/wiki/{concept}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the first paragraph of the concept
    p_tags = soup.find_all('p')
    for tag in p_tags:
        if tag.get_text(strip=True):
            description = tag.get_text(strip=True)
            break

    # Get the main image of the concept
    table = soup.find('table', class_='infobox')
    if table:
        image = table.find('img')
        image_src = f"https:{image['src']}" if image else None
    else:
        image_src = None

    return description, image_src
```