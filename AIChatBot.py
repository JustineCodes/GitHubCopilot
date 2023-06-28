# Create chatbot that will take in user input, ask ChatGPT, and return the response.

import openai
import json
import secrets

openai.api_key = secrets.OPENAI_API_KEY

def chat_with_gpt(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=100,
        temperature=0.6,
        n=1,
        stop=None,
        timeout=15,
        )
    reply = response.choices[0].text.strip()
    return reply

while True:
    user_input = input("You: ")
    response = chat_with_gpt(user_input)
    print("ChatGPT: " + response)


