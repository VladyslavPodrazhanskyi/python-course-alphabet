from pprint import pprint
import json

with open("movies.json") as file:
    movies_list = json.load(file)

print(type(movies_list))

for movie in movies_list:
    for k, v in movie.items():
        print(k, v)
