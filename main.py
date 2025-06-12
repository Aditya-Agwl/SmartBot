from agents.nlu_agent import parse_user_input
from agents.ask_questions import ask_follow_up_questions
from agents.query_generator import generate_final_query
from agents.search_agent import search_web
from agents.scraping_agent import scrape_page
from agents.analyzer_agent import analyze_results
import openai

def pipeline_search(query):
    print("\n🔍 Searching the web...")
    try:
        results = search_web(query)
        print(f"🔗 Found {len(results)} results. Scraping top pages...")
    except Exception as e:
        print(f"❌ Search failed: {e}")
        return

    scraped_data = []
    for r in results[:5]:  # Limit to top 5 results
        try:
            scraped = scrape_page(r["link"])
            scraped_data.append(scraped)
        except Exception as e:
            print(f"❌ Scraping failed for {r['link']}: {e}")

    print("\n🧠 Analyzing results...")
    try:
        analyzed = analyze_results(query, scraped_data)
    except Exception as e:
        print(f"❌ Analysis failed: {e}")
        return

    print("\n🎯 Top Recommendations:\n")
    for i, res in enumerate(analyzed[:5]):  # Display top 5 recommendations
        print(f"Recommendation {i+1}:")
        print(f"🔗 {res['url']}")
        print(f"🏷️  Title: {res.get('title', 'N/A')}")
        print(f"📄 Snippet: {res.get('body', '')[:300]}...")
        print(f"📊 Relevance Score: {res['score']:.2f}\n")


def main():
    print("🤖 Hello! What would you like to buy today?")
    user_input = input("You: ")

    print("\n🧠 Understanding your request...")
    nlu = parse_user_input(user_input)
    print("📦 NLU Output:", nlu)

    intent = nlu.get("intent")
    category = nlu.get("category")
    entities = nlu.get("entities", {})
    missing = nlu.get("missing", [])

    entities_with_category = entities.copy()
    if category:
        entities_with_category["category"] = category

    if intent and missing:
        questions = ask_follow_up_questions(intent, entities_with_category)
        for q in questions:
            print(f"\n🤔 {q}")
            ans = input("You: ")
            entities_with_category[q.lower()] = ans

    final_query = generate_final_query(intent, entities_with_category)
    print("\n🔧 Final search query:", final_query or user_input)

    pipeline_search(final_query or user_input)

if __name__ == "__main__":
    main()
