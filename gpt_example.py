import openai
import os
import sys

# Fallback to hardcoded value if environment variable is not set
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY") or "sk-YOURKEYHERE"

if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

openai.api_key = OPENAI_API_KEY

preheader = "You are a friendly assistant"

prompt = input("Your prompt here: ")

def generate_response():
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": preheader},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200
    )

response = generate_response()
assistant_message = response['choices'][0]['message']['content']
print(assistant_message)
