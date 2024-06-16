import json

with open("data.json", "r") as file:
    data = json.load(file)
    # print the number of superheroes
    print(len(data))
    print(data[0]["creator"].split(",")) # print the creators of the first superhero