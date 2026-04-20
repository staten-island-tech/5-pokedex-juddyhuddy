import json
# ## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
# ## create variable "data" that represents the enitre pokedex list
pokemons = json.load(pokedex)
# print(data[0])

# # Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
# x=0
# while x < 809:
#     print(data[x]["name"])
#     x += 1


# Add a language choice feature and print the pokemons name based on the user input
moves = open("./moves.json", encoding="utf8")
data = json.load(moves)
# print(data[0])
# x=0
# while x < 809:
#     print(data[x]["name"])
#     x += 1
# y = (input("what language?"))
# x = 0
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
# while y == "english" and x < 809:
#     print(data[x]["name"]["english"])
#     x += 1
# x = 0
# while y == "chinese" and x < 809:
#     print(data[x]["name"]["chinese"])
#     x += 1
# x = 0
# while y == "japanese" and x < 809:
#     print(data[x]["name"]["japanese"])
#     x += 1
# x = 0
# while y == "french" and x < 809:
#     print(data[x]["name"]["french"])
#     x += 1

    
# #Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


# pokemon = (input("which pokemon")).capitalize()
# x=0


# for poke in data:
#     if pokemon in poke['name']['english']:
#         print(poke['name']['english'])
#     else:
#         x += 1
#     if x > 808:
#         print("none Found!")
 #
 # 
 # 
 # For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has available based on type

pokemon = (input("what pokemon")).capitalize()
types = []
abilites = []
for poke in pokemons:
    if pokemon in poke['name']['english']:
        for type in poke['type']:
            types.append(type)

for poke_type in types:
    for move in data['type']:
        if poke_type in move:
            abilites.append(data['ename'])

print(type)
print(abilites)