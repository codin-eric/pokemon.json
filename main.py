"""
Codigo muy rapido para hacer un pokedex

Todos:
    - Validar que el numero ingresado sea un numero
    - Hacer otras funcionalidades
    - Mostrar la imagen del pokemon
    - Mostrar toda la data que hay sobre el pokemon
"""

import json


def get_by_id(numero):
    with open("pokedex.json") as json_file:
        data = json.load(json_file)
        poke = data[int(numero) - 1]

        print(f'id: {poke["id"]}')
        print(f'Nombre: {poke["name"]["english"]}')
        print(f'tipo: {poke["type"]}')
        print(f"Stats: ")
        print(f'       HP: {poke["base"]["HP"]}')
        print(f'       Attack: {poke["base"]["Attack"]}')
        print(f'       Defensa: {poke["base"]["Defense"]}')
        print(f'       Sp. Attack: {poke["base"]["Sp. Attack"]}')
        print(f'       Sp. Defense: {poke["base"]["Sp. Defense"]}')
        print(f'       Speed: {poke["base"]["Speed"]}')


numero = input("Ingrese el numero de pokemon ")
get_by_id(numero)
