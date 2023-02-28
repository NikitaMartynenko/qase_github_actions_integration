import requests
from qaseio.pytest import qase
from config import api_token



@qase.title("Получить первого существующего персонажа по ID")
def test_swapi_get():
    url = 'https://swapi.dev/api/people/1/'
    #@qase.step('Отправить get запрос:')
    response = requests.get(url)
    name = response.json()['name']
    #@qase.step('Проверить, что полученное имя совпадает с expected name')
    assert name == 'Luke Skywalker', f'actually name is {response.json()["name"]}'



@qase.title("Получить второго существующего персонажа по ID")
def test_swapi_get_2():
    url = 'https://swapi.dev/api/people/2/'
    response = requests.get(url)
    name = response.json()['name']
    assert name == 'Luke Skywalker', f'actually name is {response.json()["name"]}'









