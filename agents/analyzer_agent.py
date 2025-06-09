class AnalyzerAgent:
    def analyze(self, scraped_data, keywords):
        # Simple keyword match scoring
        def score(item):
            return sum(1 for word in keywords if word.lower() in item['title'].lower())

        scored = sorted(scraped_data, key=score, reverse=True)
        return scored[:5]  # Top 5 results
