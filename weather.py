import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data['cod'] == '404':
        print(f"Error: {weather_data['message']}")
    else:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        humidity = weather_data['main']['humidity']

        return f"""
🌡Havo harorati : {round(temperature-273.15)} °C
🌄 Havo holati: {description}
💨 Shamol tezligi: {wind_speed} m/s
🌊 Namlik: {humidity} %
    """


