from requests import get

link = "https://api.publicapis.org/entries"
parameters = {"title": "dog"}

response = get(link, params=parameters)

for entry in response.json()["entries"]:
    print(entry["API"])