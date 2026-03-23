import requests

city = input("Введите город: ")
api_key = "KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

data = requests.get(url).json()

if data.get("cod") != 200:
    print("Ошибка:", data.get("message"))
else:
    print("Температура:", data["main"]["temp"], "°C")
    print("Ощущается:", data["main"]["feels_like"], "°C")
    print("Ветер:", data["wind"]["speed"], "м/с")
    print("Давление:", data["main"]["pressure"], "гПа")
    print("Влажность:", data["main"]["humidity"], "%")
    print("Погода:", data["weather"][0]["description"])