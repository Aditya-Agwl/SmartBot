# agents/analyzer_agent.py
from difflib import SequenceMatcher

def score_similarity(query, text):
    return SequenceMatcher(None, query.lower(), text.lower()).ratio()

def analyze_results(query, scraped_data):
    scored = []
    for item in scraped_data:
        text = item.get("title", "") + " " + item.get("body", "")
        score = score_similarity(query, text)
        item["score"] = score
        scored.append(item)
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:5]  # Top 5 results
