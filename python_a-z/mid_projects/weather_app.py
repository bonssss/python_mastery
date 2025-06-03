import requests
url ="https://api.openweathermap.org/data/2.5/weather/?q=pakistan&appid=your_api_key"


def get_weather():
    try:
        city = input("Enter the city name: ")
        response = requests.get(url.replace("pakistan", city))
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather = data['weather'][0]
            print(f"Weather in {city}:")
            print(f"Temperature: {main['temp']}K")
            print(f"Humidity: {main['humidity']}%")
            print(f"Weather: {weather['description']}")
        else:
            print("City not found. Please check the name and try again.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
def main():
    while True:
        print("\nWeather App")
        print("1. Get Weather")
        print("2. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            get_weather()
        elif choice == '2':
            print("Exiting the Weather App.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()