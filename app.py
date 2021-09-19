from flask import Flask
from flask import request
import json
from twilio import twiml
from twilio.twiml.messaging_response import Body, Message, MessagingResponse
import time
from types import CoroutineType
from time import sleep
import threading
import signal
import requests

##############################


app = Flask(__name__) 

@app.route('/')
def home():
    return "Hello"

@app.route('/transitapi',methods = ['POST'])
def transitprocess():
    jsondata = request.get_json()
    data = json.loads(jsondata)

    if data['BUSID'] == '123':

        result = {'Bus Stop':'15 Minutes Away'
        }
        return json.dumps(result)

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    my_list = message_body.split(",")

    
    while True:
        try:
            if my_list[0] == 'directions':
                address = my_list[1]
                address2 = my_list[2]

                #To get long and lat for first addy
                url = "https://api.geoapify.com/v1/geocode/autocomplete?text="+address+"&type=street&apiKey=5740005f049146be9b4392e52c07fec3"

                payload={}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                print(response.text)

                j = response.text

                jsonStr = json.loads(j)

                long = jsonStr['features'][0]['properties']['lon']

                print(long)

                lat = jsonStr['features'][0]['properties']['lat']

                print(lat)


                #To get long and lat for second addy
                url2 = "https://api.geoapify.com/v1/geocode/autocomplete?text="+address2+"&type=street&apiKey=5740005f049146be9b4392e52c07fec3"

                payload={}
                headers = {}

                response2 = requests.request("GET", url2, headers=headers, data=payload)

                print(response2.text)

                j2 = response2.text

                jsonStr2 = json.loads(j2)

                long2 = jsonStr2['features'][0]['properties']['lon']

                print(long2)

                lat2 = jsonStr2['features'][0]['properties']['lat']

                print(lat2)


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

                resp = MessagingResponse()
                resp.message(removecomma)
                
                return str(resp)
            break
        except:
            break 



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
