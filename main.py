from agents.search_agent import SearchAgent
from agents.scraping_agent import ScrapingAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.nlu_agent import parse_user_input

def extract_keywords(user_input):
    # Naive keyword splitting – replace with NLP later
    return user_input.lower().split()

def main():
    user_input = input("What are you looking for? ")
    keywords = extract_keywords(user_input)

    search_agent = SearchAgent()
    scraping_agent = ScrapingAgent()
    analyzer_agent = AnalyzerAgent()

    print("\n🔍 Searching the web...")
    urls = search_agent.search(user_input)

    print("\n🕸️ Scraping content...")
    scraped_data = scraping_agent.scrape(urls)

    print("\n🧠 Analyzing results...")
    results = analyzer_agent.analyze(scraped_data, keywords)

    print("\n✅ Top Recommendations:")
    for idx, res in enumerate(results, 1):
        print(f"{idx}. {res['title']} - {res['url']}")

if __name__ == "__main__":
    main()
