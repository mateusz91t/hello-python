import requests
from x_data import weather_key, weather_host

def get_current_temp(city_name: str) -> str:
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"q":f"{city_name},pl","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"metric"}
    headers = {
        'x-rapidapi-key': weather_key,
        'x-rapidapi-host': weather_host
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.status_code

cities = ['Warsaw', 'Radom', 'Lublin']

for city in cities:
    print(get_current_temp(city))
