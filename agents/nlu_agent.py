# agents/nlu_agent.py
import os
import json
from google import genai

# Initialize Gemini
client = genai.Client(api_key="AIzaSyAZOt0p0qkKaPmXy8ElPv6ekHM0dmetbpw")

# Define what fields are expected per intent
EXPECTED_FIELDS = {
    "shop_product": ["product", "brand", "budget", "platform", "color", "type", "features"],
    "book_movie_ticket": ["movie_name", "location", "time", "format", "seat_type"],
    "flight_booking": ["from", "to", "date", "budget", "airlines", "class"],
    "travel_plan": ["from", "to", "date", "mode", "duration"]
}

def parse_user_input(user_input):
    prompt = f"""
You are an NLU agent. Your job is to analyze user input, identify their intent, and extract any known entities.

Then, based on the intent, identify which expected entities are still missing.

Output this strictly in JSON format like:
{{
  "intent": "shop_product",
  "category": "headphones",
  "entities": {{
    "product": "headphones",
    "brand": ["boAt", "JBL"],
    "budget": "2000",
    "platform": ["Flipkart", "Amazon"]
  }},
  "missing": ["type", "color", "features"]
}}

Only include `category` if applicable (e.g., for shopping).

User input: "{user_input}"
ONLY return a valid JSON object. Do not include markdown or extra commentary.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # or gemini-1.5-pro if you're using that
            contents=prompt
        )
        result = response.text.strip()

        # Clean up just in case
        result = result.replace("```json", "").replace("```", "")

        return json.loads(result)
    except Exception as e:
        print("❌ Failed to parse NLU output:", e)
        print("Raw output:", result)
        return {"intent": None, "entities": {}, "missing": []}
