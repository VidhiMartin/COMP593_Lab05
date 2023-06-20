'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    if poke_info is not None:
        print_pokemon_info(poke_info)
    return

#Added new function:
def print_pokemon_info(pokemon_info):
    name = pokemon_info.get('name', '')
    id = pokemon_info.get('id', '')
    type = ', '.join(t['type']['name'] for t in pokemon_info.get('type', []))
    abilities = ', '.join(a['ability']['name'] for a in pokemon_info.get('abilities', []))


    print(f'Name: {name}\nID: {id}\nType: {type}\nAbilities: {abilities}')




def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    pokemon_name = pokemon_name.lower().strip()
    # TODO: Build a clean URL and use it to send a GET request
    clean_url = f'{POKE_API_URL}{pokemon_name}'
    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    response = requests.get(clean_url)
    if response.status_code == requests.codes.ok:
        return response.json()
    # TODO: If the GET request failed, print the error reason and return None
    print(f'Request failed: {response.status_code} ({response.reason})')

    return

if __name__ == '__main__':
    main()