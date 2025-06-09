import requests
from bs4 import BeautifulSoup

class ScrapingAgent:
    def scrape(self, urls):
        product_data = []
        for url in urls:
            try:
                response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.title.string if soup.title else "No title found"
                product_data.append({'title': title, 'url': url})
            except Exception as e:
                print(f"Error scraping {url}: {e}")
        return product_data
