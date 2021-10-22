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
from features import *
##############################

lang_en = {
    "define_command": "define",
    "advice_command": "advice",
    "joke_command": "joke",
    "search_command": "search",
    "crypto_command": "crypto",
    "directions_command": "directions",
    "transit_command": "transit"
}

lang_es = {
    "define_command": "definir",
    "advice_command": "consejo",
    "joke_command": "chiste",
    "search_command": "buscar",
    "crypto_command": "criptomoneda",
    "directions_command": "direcciones",
    "transit_command": "transito"
}

lang = lang_en

app = Flask(__name__) 

@app.route('/')
def home():
    return "Hello"


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    message_body = message_body.split(',')
    resp = MessagingResponse()
    key_command = message_body[0]
    if len(message_body) > 1:
        user_parameter = message_body[1]

    if key_command == lang["define_command"]:
        resp.message(get_definition(user_parameter))
        return str(resp)
    elif key_command == lang["advice_command"]:
        resp.message(random_advice())
        return str(resp)
    elif key_command == lang["joke_command"]:
        resp.message(give_joke())
        return str(resp)
    elif key_command == lang["search_command"]:
        resp.message(search_google(user_parameter))
        return str(resp)
    elif key_command == lang["crypto_command"]:
        resp.message(crypto(user_parameter))
        return str(resp)
    elif key_command == lang["directions_command"]:
        resp.message(directions(user_parameter, message_body[2]))
        return str(resp)
    elif key_command == lang["transit_command"]:
        resp.message(transit(user_parameter, message_body[2]))
        return str(resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
