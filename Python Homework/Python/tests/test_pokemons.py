import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'trainer_token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN} 
TRAINER_ID = '37948'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]["name"] == 'New Name'

@pytest.mark.parametrize('key, value', [('name', 'New Name'), ('trainer_id', TRAINER_ID), ('id', '374818')])

def test_paramertize(key, value):  
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})

    assert response_get.json()['data'][0][key] == value
