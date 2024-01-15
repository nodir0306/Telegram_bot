import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
    }
   #regions = ["", "", "", "", "Fergana", "Namangan", "Bukhara", "Qarshi", "Navoiy", "Khiva", "Guliston", "Samarkand"]
    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data['cod'] == '404':
        print(f"Error: {weather_data['message']}")
    else:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        humidity = weather_data['main']['humidity']

        return weather_data['weather'][0]

# Provide your API key and city name when calling the function
api_key = "9215939b9dcd31fb5ec0ee3455e34ee4"
city_name = "Tashkent"
print(get_weather(api_key, city_name))
