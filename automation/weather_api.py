import requests

API_KEY = '7451afdbc72e4b4f210799ff444358da'
city = input('Enter a city name: ')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
request_url = f'{BASE_URL}?q={city}&appid={API_KEY}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    description = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    weather_type = data['weather'][0]['main']
    feels_like = round(data['main']['feels_like'] - 273.15, 2)
    min_temp = round(data['main']['temp_min'] - 273.15, 2)
    max_temp = round(data['main']['temp_max'] - 273.15, 2)
    pressure = data['main']['pressure'] # in hPa
    humidity = data['main']['humidity'] # in %
    visibility = data['visibility'] # in km

    print(data)
    print('Weather description: ', description)
    print('Temperature: ', temperature, 'degree celsius')
    print('Latitude: ', latitude)
    print('longitude: ', longitude)
    print('weather_type: ', weather_type)
    print('feels_like: ', feels_like)
    print('min_temp: ', min_temp)
    print('max_temp: ', max_temp)
    print('pressure: ', pressure)
    print('humidity: ', humidity)
    print('visibility: ', visibility)
else:
    print('An error occured')



'''
{'coord': {'lon': 3.8964, 'lat': 7.3878}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'base': 'stations', 'main': {'temp': 302.18, 'feels_like': 304.71, 'temp_min': 302.18, 'temp_max': 302.18, 'pressure': 1012, 'humidity': 63, 'sea_level': 1012, 'grnd_level': 987}, 'visibility': 10000, 'wind': {'speed': 2.48, 'deg': 206, 'gust': 2.69}, 'rain': {'1h': 0.35}, 'clouds': {'all': 100}, 'dt': 1654947742, 'sys': {'country': 'NG', 'sunrise': 1654925269, 'sunset': 1654970427}, 'timezone': 3600, 'id': 2339354, 'name': 'Ibadan', 'cod': 200}

Weather description:  light rain
Temperature:  29.03 degree celsius
Latitude:  7.3878
longitude:  3.8964
weather_type:  Rain
feels_like:  31.56
min_temp:  29.03
max_temp:  29.03
pressure:  1012
humidity:  63
visibility:  7.3878
Latitude:  10000

'''
# lat, lon, weather-main, description,