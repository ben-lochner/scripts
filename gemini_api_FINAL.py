import json
from google import genai
from google.genai import types

client = genai.Client()

def get_validated_input(prompt_message: str) -> str:
    while True:
        user_input = input(prompt_message).strip()

        if not user_input:
            print("Input cannot be empty! Please enter a response.")
            continue

        return user_input

while True:
    prompt = get_validated_input("Prompt: ")

    if prompt.lower() in ['exit', 'quit']:
        print("Great session! See you next time!")
        break

    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are a strict but caring Socratic educator."
                    "You never outright reveal answers to students, but you do assist and aid their desire for knowledge."
                    "Return a JSON object with 'hint' and 'question' fields to help the student."
                ),
                response_mime_type="application/json",
                temperature=0.77,
                top_p=0.90,
                top_k=25,
            ),
        )

        raw_text_data = response.text
        filtered_data = raw_text_data.strip()
        parsed_data = json.loads(filtered_data)

        print("Parsed Object Type:", type(parsed_data))
        print("Hint:", parsed_data.get("hint"))
        print("Question:", parsed_data.get("question"))

    except Exception as e:
        print(f"An error occurred during the loop: {e}")
        break
