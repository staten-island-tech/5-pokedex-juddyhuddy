# import json
# ## Open the JSON file of pokemon data
# pokedex = open("./pokedex.json", encoding="utf8")
# ## create variable "data" that represents the enitre pokedex list
# data = json.load(pokedex)
# print(data[0])

# # Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
# x=0
# while x < 809:
#     print(data[x]["name"])
#     x += 1


# Add a language choice feature and print the pokemons name based on the user input
import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
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

    
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has available based on type
pokemon = (input("which pokemon"))
x=0

while x < 809:
    if pokemon == (data[x]["name"]["english"]): 
        print(data[x]["name"]["english"])
        x+=1

    elif x == 809 and pokemon != data[x]["name"]["english"]:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        print("pokemon not found")       
       


    