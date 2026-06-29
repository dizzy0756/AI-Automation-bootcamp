import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to retrieve data. {response.status_code}"

name = input("Enter the name of the pokemon : ")
pokemon_info = get_pokemon_info(name)
if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Height : {pokemon_info['height']}")