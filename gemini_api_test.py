from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=types.Part.from_text(text=str(input("Prompt: "))),
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a strict but caring Socratic educator."
            "You never outright reveal answers to students, but you do assist and aid their desire for knowledge."
        ),
        temperature=0.77,
        top_p=0.90,
        top_k=25,
    ),
)

print(response.text)
