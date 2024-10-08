import requests
import json

url = "https://open.er-api.com/v6/latest/USD"#ссылка на сайт с которого хотим получить информацию
api_info_usd = requests.get(url)#ответ на запрос на получение данных
print(api_info_usd)#

if  api_info_usd.status_code == 200:#провераем статус кода(успешин зпарос или нет)
    convertal = api_info_usd.json()#она переводить к json формату
    #json - это формат хранения данных
    print("успешно")
    print(f"1 usd = {convertal['rates']['UAH']}гривен")
    print(f"1 usd = {convertal['rates']['EGP']}фунт египетский")

else:
    print("error")
    print(f"ошибка под номером {api_info_usd.status_code}")