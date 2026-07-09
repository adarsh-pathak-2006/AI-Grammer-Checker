import json
from services.build_prompt import build_prompt
from services.ai_integration import generate_response

def get_response(input):
    final_prompt=build_prompt(input=input)
    output=generate_response(final_prompt)

    raw_text = output.text.strip()
    try:
        # Since we enforced JSON mime type, this should be valid JSON
        return json.loads(raw_text)
    except Exception as e:
        # Fallback if Gemini somehow includes markdown backticks anyway
        raw_text = raw_text.removeprefix("```json").removesuffix("```").strip()
        try:
            return json.loads(raw_text)
        except Exception:
            return {
                "corrected_text": raw_text,
                "mistakes": ["Format error"],
                "explanation": "Failed to parse AI output into strict JSON format."
            }

