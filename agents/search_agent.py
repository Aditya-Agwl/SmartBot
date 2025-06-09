from duckduckgo_search import DDGS

class SearchAgent:
    def search(self, query, num_results=5):
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=num_results):
                results.append(r["href"])
        return results
