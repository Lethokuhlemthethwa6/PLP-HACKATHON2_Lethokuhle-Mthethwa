import openai # pyright: ignore[reportMissingImports]
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_tip(mood_text):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Suggest 1 short self-care tip if someone says: {mood_text}",
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception:
        return "Take a deep breath and relax 🌿"
