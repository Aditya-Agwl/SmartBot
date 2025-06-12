from google import genai
import json

client = genai.Client(api_key="AIzaSyAZOt0p0qkKaPmXy8ElPv6ekHM0dmetbpw")

def generate_final_query(intent, entities_with_category):
    prompt = f"""
You are a query generator for a shopping assistant, optimizing for DuckDuckGo search. Your goal is to create the BEST possible search query for finding products online.

Intent: {intent}
Entities and preferences: {json.dumps(entities_with_category)}

Based on the intent and entities, generate a concise and effective search query that is a well-formed English sentence.
The query should be optimized for online shopping using DuckDuckGo and include relevant keywords.

Examples:
- If intent is "shop_product" and entities are {{"product": "shoes", "brand": "Nike", "color": "red"}}, the query should be: "Buy red Nike shoes online"
- If intent is "book_movie_ticket" and entities are {{"movie_name": "Oppenheimer", "location": "New York"}}, the query should be: "Find Oppenheimer movie tickets in New York"

Here are some guidelines for generating the query, optimized for DuckDuckGo:
- Always include the product name if available.
- Include brand names if specified.
- Include key features or attributes (e.g., color, size, type).
- Use action words like "buy", "shop for", "find" to improve search relevance.
- If a budget is specified, include it using "under" or "less than" (e.g., "under $3000").
- Prioritize the most important entities for a focused search.
- Use specific keywords rather than long phrases.
- Consider common search terms that users might enter on DuckDuckGo.
- Structure the query as a natural-sounding English sentence for better readability and relevance.

Return only the query text.
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print("❌ Failed to generate search query:", e)
        return ""
