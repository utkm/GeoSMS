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


# trivia me
def trivia_question():
    base_url = "https://opentdb.com/api.php?amount=1&type=boolean"
    parent = requests.get(base_url).json()
    question = parent["results"][0]["question"]
    question = question.replace("&#039;", "\'")
    question = question.replace("&quot;", "\"")
    
    answer = parent["results"][0]["correct_answer"]
    return question, answer
#print(trivia_question())


# joke
def give_joke():
    base_url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
    parent = requests.get(base_url).json()
    joke = parent["joke"]
    return joke
#print(give_joke())


# search (query)
def search_google(query):
    base_url = "https://api.scaleserp.com/search"
    params = {
        'api_key': '3D2B8CEFBAA54A3BB59FDA4FFC6D51E9',
        'q': query
    }
    parent = requests.get(base_url, params).json()
    answer = parent["answer_box"]["answers"][0]["answer"].split('.')
    answer = answer[:1]
    return answer[0]
#print(search_google("do sharks eat humans?"))