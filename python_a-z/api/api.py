import requests

url ="https://api.openweathermap.org/data/2.5/weather/?q=pakistan&appid=b4aac90b73577323689d210536680923"


response=   requests.get(url)
if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    print(f"Temperature in Aaais: {temperature}K")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")