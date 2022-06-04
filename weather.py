from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather(request) -> str:
    request = request.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={request}&oq={request}'
        f'&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    precipitation = soup.select('#wob_pp')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()

    return f'{location}\n{time}\n{info}\nВероятность осадков: {precipitation}\n{weather} °C'


def weather_today() -> str:
    temper = []
    time = 2
    res = requests.get('https://www.gismeteo.ru/weather-kaliningrad-4225/', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('[class~=widget-row-chart-temperature]')[0]
    for i in location.select('[class~=unit_temperature_c]'):
        temper += [f'В {time}:00 температура {i.get_text()}']
        time += 3
    temp_list = '\n'.join(temper)
    print(temp_list)
    return f'{temp_list}'

def weather_tomorrow() -> str:
    temper = []
    time = 2
    res = requests.get('https://www.gismeteo.ru/weather-kaliningrad-4225/tomorrow/', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('[class~=widget-row-chart-temperature]')[0]
    for i in location.select('[class~=unit_temperature_c]'):
        temper += [f'В {time}:00 температура {i.get_text()}']
        time += 3
    temp_list = '\n'.join(temper)
    print(temp_list)
    return f'{temp_list}'