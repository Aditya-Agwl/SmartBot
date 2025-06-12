# agents/search_agent.py
from googleapiclient.discovery import build

# Set your Google Custom Search API key and CX (search engine ID)
API_KEY = "AIzaSyDkwiJQAldkr86VnxywwCWSMiRHnJ1zVjE"
CX = "f53ac7621a00e461e"

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
