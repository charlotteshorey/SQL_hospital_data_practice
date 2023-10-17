import requests  # for requesting API. No keys necessary
import random  # to generate random numbers. Used for random pokemon id and moves
print("\nWelcome. You will be assigned a random Pokemon to look after. Lucky you!")

# random number generator of pokemon ids 1-1017

def get_random_pokemon():
    random_poke_id = random.randint(0, 1016)
    url = "https://pokeapi.co/api/v2/pokemon/{}".format(random_poke_id)
    response = requests.get(url)
    pokemon = response.json()   # retrieving the random pokemon data from the API
    users_pokemon = pokemon["name"]
    return users_pokemon


assigned_pokemon_1 = get_random_pokemon()
assigned_pokemon_msg = f"\nYour assigned pokemon is {assigned_pokemon_1}"
print(assigned_pokemon_msg)

# loop for user being happy with pokemon or not
while True:
    user_happy = input("Are you happy with this pokemon? (yes/no) ")
    if user_happy.lower() == "yes":
        print("Aw, they will be so happy too!")
        break
    elif user_happy.lower() == "no":
        print(f"\nOUCH! That's kinda mean... You have made them upset.\nI guess you can have one more try...")
        assigned_pokemon_1 = get_random_pokemon()
        print(assigned_pokemon_msg[0:26:] + assigned_pokemon_1, "and you cannot swap again because you were mean.")
        break
    else:
        print("\nPlease try again, I don't understand")

# now user has a pokemon
# access the users pokemons moves from API and select random ones


def get_pokemon_moves():
    url = "https://pokeapi.co/api/v2/pokemon/{}".format(assigned_pokemon_1)
    response = requests.get(url)
    pokemon = response.json()  # retrieving the random pokemon data from the API
    moves_values = pokemon["moves"]
    rand_value = random.choice(list(moves_values))
    move_name = rand_value["move"]["name"]

    return move_name


moves = f"{get_pokemon_moves()}\n{get_pokemon_moves()}\n{get_pokemon_moves()}"

print("\nHave a look at your Pokemons' moves in the created text file!")


# write final pokemon and random moves into a file

with open("Your_Pokemon.txt", "w") as poke_file:
    poke_file.write("Your Pokemon:\n" + assigned_pokemon_1 + "\n\nIts random moves are:\n" + moves +
                    "\n\nTake good care of your Pokemon!")
poke_file.close()
