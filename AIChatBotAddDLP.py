# Create chatbot that will take in user input, ask ChatGPT, and return the response.

import openai, json, secrets, my_secrets
import os
from nightfall.client import NightfallClient
from nightfall.config import NightfallConfig
from nightfall.scan import ScanRequest

openai.api_key = my_secrets.OPENAI_API_KEY

with open('api_key.txt', 'r') as f:
    api_key = f.read().strip()

nightfall_config = NightfallConfig(api_key)
nightfall_client = NightfallClient(nightfall_config)



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
    payload = [user_input]
    detection_rule_uuids = ['9a134234-d8e1-43b5-b861-ddbfa5f84097']
    scan_request = ScanRequest(payload=payload, detection_rule_uuids=detection_rule_uuids)
    if nightfall_client.scan(scan_request).is_sensitive:
        print("ChatGPT: Sorry, I can't answer that.")
    elif user_input.lower() in ['quite', 'exit']:
        print("ChatGPT: Goodbye!")
        break
    else:
        response = chat_with_gpt(user_input)
        print("ChatGPT: " + response)
