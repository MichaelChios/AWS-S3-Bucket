import json

filtered_data = []
with open("data.json", "r") as file:
    raw_data = json.load(file)
    clean_data = [superhero for superhero in raw_data if len(superhero) == 12]
    for i in range(len(clean_data)):
        filtered_data.append({"id": clean_data[i]["id"], "name": clean_data[i]["name"], "description": clean_data[i]["description"],
                          "powers": clean_data[i]["powers"], "quotes": clean_data[i]["quotes"],
                          "affiliation": clean_data[i]["affiliation"], "creators": clean_data[i]["creator"],
                          "aka": clean_data[i]["aka"]})
        
    for i in range(len(filtered_data)):
        filtered_data[i]["id"] = i+1
        
with open("filtered_data.json", "w") as file:
    json.dump(filtered_data, file, indent=4)
    print("Data filtered successfully!")