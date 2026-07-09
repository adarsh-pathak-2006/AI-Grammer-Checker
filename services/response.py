from services.build_prompt import build_prompt
from services.ai_integration import generate_response

def get_response(input):
    final_prompt=build_prompt(input=input)
    output=generate_response(final_prompt)

    return output

