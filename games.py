import requests, json

# format: define (word)
def get_definition(word):
    base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    parent = requests.get(base_url+word).json()
    definition = parent[0]["meanings"][0]["definitions"][0]["definition"]
    return definition
#print(get_definition("Salubrious"))

# format: random advice
def random_advice():
    base_url = "https://api.adviceslip.com/advice"
    parent = requests.get(base_url).json()
    advice = parent["slip"]["advice"]
    return advice
#print(random_advice())

