from google import genai
from django.conf import settings

client = None

def get_client():
    global client
    if client is None:
        if not settings.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set. Add it to your .env file.")
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
    return client


from google.genai import types

def generate_response(prompt):
    response = get_client().models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        )
    )
    return response