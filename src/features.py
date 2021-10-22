import requests, json

# format: define, (word)
def get_definition(word):
    base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    parent = requests.get(base_url+word).json()
    definition = parent[0]["meanings"][0]["definitions"][0]["definition"]
    return definition
#print(get_definition("Salubrious"))


# format: advice
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

# crypto,eth
def crypto(cryptoname):
    name = cryptoname
    realcrp = name.upper()
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol="+realcrp+""
    payload={}
    headers = {
    'X-CMC_PRO_API_KEY': '040e1fec-997b-4f47-aecc-8be3ec15760c'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    crp = response.text

    stepsjson2 = json.loads(crp)

    price = stepsjson2['data'][realcrp]['quote']['USD']['price']

    p24change = stepsjson2['data'][realcrp]['quote']['USD']['percent_change_24h']

    finalret = "The Current Value Of "+str(realcrp)+" Is "+str(price)+" Dollars And The Percent 24 Hour Change Is "+str(p24change)+""

    return str(finalret)

# directions,address1,address2
def directions(address, address2):
    #To get long and lat for first addy
    url = "https://api.geoapify.com/v1/geocode/autocomplete?text="+address+"&type=street&apiKey=5740005f049146be9b4392e52c07fec3"

    payload={}
    headers = {}  

    response = requests.request("GET", url, headers=headers, data=payload)

    #print(response.text)

    j = response.text

    jsonStr = json.loads(j)

    long = jsonStr['features'][0]['properties']['lon']

    #print(long)

    lat = jsonStr['features'][0]['properties']['lat']

    #print(lat)


    #To get long and lat for second addy
    url2 = "https://api.geoapify.com/v1/geocode/autocomplete?text="+address2+"&type=street&apiKey=5740005f049146be9b4392e52c07fec3"

    payload={}
    headers = {}

    response2 = requests.request("GET", url2, headers=headers, data=payload)

    #print(response2.text)

    j2 = response2.text

    jsonStr2 = json.loads(j2)

    long2 = jsonStr2['features'][0]['properties']['lon']

    #print(long2)

    lat2 = jsonStr2['features'][0]['properties']['lat']

    #print(lat2)


    url = "https://api.geoapify.com/v1/routing?waypoints="+str(lat)+","+str(long)+"|"+str(lat2)+","+str(long2)+"&mode=walk&lang=en&apiKey=5740005f049146be9b4392e52c07fec3"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    d = response.text

    stepsjson = json.loads(d)


    instructions = stepsjson['features'][0]['properties']['legs'][0]['steps']

    print('###########################')

    directions = []

    for item in instructions:
        x = item['instruction']['text']
        y = item['distance']
        z = str(x) + " - " + "Distance " + str(y) + " Metres"
        directions.append(z)

    removesqbrackl = str(directions).replace("[", "")

    removesqbrackr = removesqbrackl.replace("]", "")

    removeqs = removesqbrackr.replace("'", "\n")

    removecomma = removeqs.replace(",", "")

    print(removecomma)

    return str(removecomma)

def transit(address, address2):
    #To get long and lat for first addy
    url = "https://api.geoapify.com/v1/geocode/autocomplete?text="+address+"&type=street&apiKey=5740005f049146be9b4392e52c07fec3"

    payload={}
    headers = {}  

    response = requests.request("GET", url, headers=headers, data=payload)
    #print(response.text)

    j = response.text

    jsonStr = json.loads(j)

    long = jsonStr['features'][0]['properties']['lon']

    #print(long)
    lat = jsonStr['features'][0]['properties']['lat']

    #print(lat)
    #To get long and lat for second addy
    url2 = "https://api.geoapify.com/v1/geocode/autocomplete?text="+address2+"&type=street&apiKey=5740005f049146be9b4392e52c07fec3"

    payload={}
    headers = {}

    response2 = requests.request("GET", url2, headers=headers, data=payload)

    #print(response2.text)

    j2 = response2.text

    jsonStr2 = json.loads(j2)

    long2 = jsonStr2['features'][0]['properties']['lon']

    #print(long2)

    lat2 = jsonStr2['features'][0]['properties']['lat']

    #print(lat2)

    url = "https://api.geoapify.com/v1/routing?waypoints="+str(lat)+","+str(long)+"|"+str(lat2)+","+str(long2)+"&mode=transit&lang=en&apiKey=5740005f049146be9b4392e52c07fec3"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    d = response.text

    stepsjson = json.loads(d)


    instructions = stepsjson['features'][0]['properties']['legs'][0]['steps']

    #print('###########################')

    directions = []

    for item in instructions:
        x = item['instruction']['text']
        y = item['distance']
        z = str(x) + " - " + "Distance " + str(y) + " Metres"
        directions.append(z)

    removesqbrackl = str(directions).replace("[", "")

    removesqbrackr = removesqbrackl.replace("]", "")

    removeqs = removesqbrackr.replace("'", "\n")

    removecomma = removeqs.replace(",", "")

    #print(removecomma)
    return removecomma
