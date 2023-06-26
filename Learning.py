# Create a hello world program

# print("Hello World")

# Create a function to get information from the web
import requests

url = "https://www.google.com"

response = requests.get(url)

print(response)