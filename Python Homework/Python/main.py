import requests  

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'trainer_token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}  


# Создание покемона:

body_сreate = {
    "name": "PeFcN",
    "photo_id": 12
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_сreate)
print(response.text)

message = response.json()['message']
print(message)

# Изменение имени

body_put = {
    "pokemon_id": "374818",
    "name": "New Name",
    "photo_id": 2
}

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put.text)

message = response_put.json()['message']
print(message)

# Поймать покемона в покебол

body_add = {
    "pokemon_id": "374818"
}

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)

message = response_add.json()['message']
print(message)



    


