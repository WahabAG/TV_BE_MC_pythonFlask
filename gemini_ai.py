# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

def generate(message):
    try:
        client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY"),
        )

        model = "gemini-3-flash-preview"
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text= message),
                ],
            ),
        ]
        generate_content_config = types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_level="HIGH",
            ),
        )

        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
        
            if chunk.text:
                print(chunk.text, end="", flush = True)
    except Exception as e: 
        return f"An error occurred: {e}"
    
if __name__ == "__main__":
    generate()


