# agents/search_agent.py
from dotenv import load_dotenv
import os
from googleapiclient.discovery import build

load_dotenv()

# Set your Google Custom Search API key and CX (search engine ID)
API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
CX = os.getenv("GOOGLE_SEARCH_CX")

def search_web(query, max_results=5):
    service = build("customsearch", "v1", developerKey=API_KEY)
    res = service.cse().list(q=query, cx=CX, num=max_results).execute()
    results = []
    for item in res.get("items", []):
        results.append({
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet", "")
        })
    return results


# # agents/search_agent.py
# from duckduckgo_search import DDGS

# def search_web(query, max_results=5):
#     results = []
#     with DDGS() as ddgs:
#         for r in ddgs.text(query, max_results=max_results):
#             results.append({"title": r['title'], "link": r['href'], "snippet": r.get("body", "")})
#     return results
