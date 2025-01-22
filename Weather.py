import requests

def get_weather(city,api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url=url)
    if response.status_code <300 or response.status_code >= 200:
        data = response.json()

        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        print(f"Weather in {city}: {weather} with temperature {temp}°C")

    else :
        print(f"Error with status code {response.status_code}")

if __name__ == "__main__":
    city = "Chennai"
    api_key = "45f7165c749b8985b633932374b0a1cb"
    get_weather(city=city,api_key=api_key)