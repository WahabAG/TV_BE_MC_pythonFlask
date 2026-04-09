# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

# def generate(message):
#     try:
#         client = genai.Client(
#             api_key=os.getenv("GEMINI_API_KEY"),
#         )

#         model = "gemini-3-flash-preview"
#         contents = [
#             types.Content(
#                 role="user",
#                 parts=[
#                     types.Part.from_text(text= message),
#                 ],
#             ),
#         ]
#         generate_content_config = types.GenerateContentConfig(
#             thinking_config=types.ThinkingConfig(
#                 thinking_level="HIGH",
#             ),
#         )

#         for chunk in client.models.generate_content_stream(
#             model=model,
#             contents=contents,
#             config=generate_content_config,
#         ):
        
#             if chunk.text:
#                 print(chunk.text, end="", flush = True)
#     except Exception as e: 
#         return f"An error occurred: {e}"
    


# simple all - In One
def generate(message):
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        # Use generate_content instead of generate_content_stream
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=message,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_level="HIGH"),
            ),
        )
        return response.text # Return the string to Flask
    except Exception as e:
        return f"Error: {e}"



# streaming
# def generate(message):
#     try:
#         client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
#         for chunk in client.models.generate_content_stream(
#             model="gemini-3-flash-preview",
#             contents=message,
#             config=types.GenerateContentConfig(
#                 thinking_config=types.ThinkingConfig(thinking_level="HIGH"),
#             ),
#         ):
#             if chunk.text:
#                 yield chunk.text  # Yielding sends chunks to the Flask generator
#     except Exception as e:
#         yield f"Error: {e}"

# def generate(message):
#     try:
#         client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
#         # We use generate_content for the "All-at-Once" approach
#         response = client.models.generate_content(
#             model="gemini-3-flash-preview",
#             contents=message,
#             config=types.GenerateContentConfig(
#                 thinking_config=types.ThinkingConfig(thinking_level="HIGH"),
#             ),
#         )
        
#         # Return the actual text string back to the Flask route
#         return response.text 
        
#     except Exception as e:
#         return f"I'm sorry, I encountered an error: {str(e)}"




if __name__ == "__main__":
    generate()


