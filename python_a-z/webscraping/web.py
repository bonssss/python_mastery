import requests

response = requests.get("https://www.google.com")
print(response)  # Print the status code of the response
print(response.text)  # Print the content of the response