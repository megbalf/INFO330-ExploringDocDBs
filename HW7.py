import sqlite3 
from pymongo import MongoClient

# Connection to Mongo
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Connecting the sqlite database 
conn = sqlite3.connect('pokemon.sqlite')
cursor = conn.cursor()

#pokemon_data = cursor.execute("select * from pokemon").fetchall()
#print(pokemon_data)

count = cursor.execute("select count(*) from pokemon").fetchone()
# print(count[0])

for i in range(1, count[0]+1):
 pokemon_info = cursor.execute("select name, pokedex_number, attack, defense, speed, sp_attack, sp_defense from pokemon").fetchall()
# print(pokemon_info)
   # print(i)



pokemon = {
       "name": pokemon_info[0],
       "pokedex_number": pokemon_info[1],
       # "types": [pokemon_info[3], pokemon_info[4]],
       #"hp": pokemon_info[5],
      "attack": pokemon_info[2],
       "defense": pokemon_info[3],
      "speed": pokemon_info[4],
      "sp_attack": pokemon_info[5],
      "sp_defense": pokemon_info[6]
       # "abilities": abilities
   }
pokemonColl.insert_one(pokemon)
print(pokemon)

pikachu_id = 25
pikachu = "select * from pokemon where pokedex_number = '" + pikachu_id + "' "
print(pikachu)
