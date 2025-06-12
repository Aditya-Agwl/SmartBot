from google import genai
import json

client = genai.Client(api_key="AIzaSyAZOt0p0qkKaPmXy8ElPv6ekHM0dmetbpw")

def ask_follow_up_questions(intent, entities_with_category):
    prompt = f"""
You are a smart shopping assistant. You already know:
Intent: {intent}
Entities so far: {json.dumps(entities_with_category)}

Ask only 3 highly relevant follow-up questions to better understand the user's needs.
Questions should be direct, short, and cover important aspects like budget, brand, type, features, or platform.
Avoid repeating or asking what you already know.

Return in this JSON format:
{{ "questions": ["question1", "question2", "question3"] }}

Ensure that the output is ALWAYS a valid JSON object. If you cannot determine the questions, return an empty JSON array.
Return ONLY the JSON object, without any markdown formatting or ```json blocks.
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        result = response.text.strip()
        # Remove ```json and ``` blocks
        result = result.replace("```json", "").replace("```", "")
        return json.loads(result).get("questions", [])
    except (json.JSONDecodeError, AttributeError) as e:
        print(f"❌ Failed to generate follow-up questions: {e}")
        return []
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return []
