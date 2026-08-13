import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def explain_with_ai(code1, code2):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Explain similarity between:\n{code1}\nAND\n{code2}"
            }]
        )
        return response["choices"][0]["message"]["content"]
    except:
        return "AI explanation unavailable"