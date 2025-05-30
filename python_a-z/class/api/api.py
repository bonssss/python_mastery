import requests

url ="https://api.openweathermap.org/data/2.5/weather/?q=pakistan&appid=your_api_key_here"


response=   requests.get(url)
if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    print(f"Temperature in Aaais: {temperature}K")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")