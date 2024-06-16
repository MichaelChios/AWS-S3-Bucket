import requests
import json

url = "https://marvel-heroic-api-unlock-the-mcu-legendary-characters.p.rapidapi.com/characters"
headers = {
	"x-rapidapi-key": "6c495789b0mshfe015a112536544p1f6c6cjsnfbbc4f1ac8b7",
	"x-rapidapi-host": "marvel-heroic-api-unlock-the-mcu-legendary-characters.p.rapidapi.com"
}

response_API = requests.get(url, headers=headers)

data = response_API.text

json_data = json.loads(data)

with open('data.json', 'w') as f:
    json.dump(json_data, f, indent=4) # save the data in a json file
    
# Print the keys so we know the columns we need to create in the database
with open('data.json', 'r') as f:
    data = json.load(f)
    for key, value in data[0].items():
        print(key)