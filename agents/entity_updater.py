# agents/entity_updater.py
from google import genai
import json

client = genai.Client(api_key="AIzaSyAZOt0p0qkKaPmXy8ElPv6ekHM0dmetbpw")

def extract_entity_from_answer(intent, previous_question, user_answer):
    prompt = f"""
You are an AI assistant. Based on the user's answer and the previous question, extract the most relevant key-value pair as a JSON entity.

Intent: {intent}
Question: "{previous_question}"
Answer: "{user_answer}"

Return a JSON object like: {{"key": "value"}} or {{"key": ["value1", "value2"]}} if multiple items were mentioned.
Only return valid JSON without any explanations or markdown.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        result = response.text.strip()
        result = result.replace("```json", "").replace("```", "")
        return json.loads(result)
    except Exception as e:
        print("❌ Failed to extract entity:", e)
        return {}
