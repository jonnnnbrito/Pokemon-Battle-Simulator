"""1. Selection of Pokemon Characters
    DONE -- Create an introduction for this game
    TODO -- The program provides a list of characters for the user (see picture).
    TODO -- Each pokemon hasa predefined base power, representing their natural strength. Power should range from weak to strong.
    TODO -- The actual power used in the battle will be a combination of the base power and a random factor between 0 and 1 (see computation).
    TODO -- Once selected, the user should be prompted by the Pokemon character and its corresponding power."""

pokemon_list = [
    {"Pokemon": "Pikachu", "Base Power": 50},
    {"Pokemon": "Charmander", "Base Power": 55},
    {"Pokemon": "Bulbasaur", "Base Power": 60},
    {"Pokemon": "Squirtle", "Base Power": 58},
    {"Pokemon": "Jigglypuff", "Base Power": 45},
    {"Pokemon": "Eevee", "Base Power": 52},
    {"Pokemon": "Snorlax", "Base Power": 80},
    {"Pokemon": "Gengar", "Base Power": 70},
    {"Pokemon": "Machamp", "Base Power": 75},
    {"Pokemon": "Mewtwo", "Base Power": 90},
]

def introduction():
    print("+-----------------------------------------------------------------------+")
    print("|               Welcome to the Pokémon Battle Simulation!               |")
    print("+-----------------------------------------------------------------------+")
    print("| Select your Pokémon character from the list below. Each Pokémon has a |")
    print("| predefined base power, representing their natural strength.           |")
    print("| The actual power used in the battle will be a combination of the base |")
    print("| power and a random factor between 0 and 1. Once selected, you will    |")
    print("| be prompted by the Pokémon character and its corresponding power.     |")
    print("+-----------------------------------------------------------------------+")
    print()

def printing_pokemon_list():
    print("+----------------+------------+")
    print("|  List of Pokemon Available  |")
    print("+----------------+------------+")
    print("|    Pokemon     | Base Power |")
    print("+----------------+------------+")
    for pokemon in pokemon_list:
        print(f"| {pokemon['Pokemon']:14} | {pokemon['Base Power']: ^10} |")
    print("+----------------+------------+")