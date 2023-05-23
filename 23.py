import requests  # импортирую библитеку requests
city = "Moscow,RU"  # запоминаю в переменную город который меня интересует
appid = "274529f20f3fe894f05c3b2e6986a9d3"  # запоминаю в переменную APPID
res = requests.get("http://api.openweathermap.org/data/2.5/weather",  # отправляем запрос на сервис.
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()  # сохраняем результат
print("Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз на неделю:")
for i in data['list']:
    print("скорость ветра <", i['wind']['speed'], "> \r\nвидимость <", i['visibility'], ">")
    print("_____________________________")
    