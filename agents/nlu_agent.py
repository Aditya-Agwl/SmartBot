import openai

openai.api_key = "YOUR_API_KEY"  # Replace with your actual key or load from env variable

def parse_user_input(user_input):
    prompt = f"""
    You are an AI agent that extracts structured intent and relevant entities from natural language input.

    Given a user query, return a JSON with the following structure:

    {{
    "intent": "<user's intent in snake_case>", 
    "entities": {{
        "product": "",
        "location": "",
        "from": "",
        "to": "",
        "date": "",
        "budget": "",
        "movie_name": "",
        "time": "",
        "platform": "",
        "brand": "",
        "category": "",
        ...
    }}
    }}

    If any information is missing, leave it as an empty string or null.

    Example:
    Query: "Book two tickets for Inception tonight in Delhi"
    →
    {{
    "intent": "book_movie_ticket",
    "entities": {{
        "movie_name": "Inception",
        "time": "tonight",
        "location": "Delhi"
    }}
    }}

    Query: "Buy a white cotton shirt under 1000 rupees from Flipkart"
    →
    {{
    "intent": "shop_product",
    "entities": {{
        "product": "white cotton shirt",
        "budget": "1000",
        "platform": "Flipkart"
    }}
    }}

    Query: "{user_input}"
    →
    """


    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant extracting intent and entities."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    # Parse JSON output
    import json
    text = response.choices[0].message.content.strip()
    try:
        parsed = json.loads(text)
        return parsed
    except json.JSONDecodeError:
        # fallback if OpenAI doesn't return perfect JSON
        return {"intent": None, "entities": {}}
