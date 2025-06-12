# agents/scraping_agent.py
import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "No title"
        body = soup.get_text(separator=' ', strip=True)[:500]  # limit to 500 chars
        return {"url": url, "title": title, "body": body}
    except Exception as e:
        return {"url": url, "error": str(e)}
