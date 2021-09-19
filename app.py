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
    user_parameter = message_body[1]

    if key_command == "define":
        resp.message(get_definition(user_parameter))
        return str(resp)
    elif key_command == "advice":
        resp.message(random_advice())
        return str(resp)
    elif key_command == "joke":
        resp.message(give_joke())
        return str(resp)
    elif key_command == "search":
        resp.message(search_google(user_parameter))
        return str(resp)
    elif key_command == "crypto":
        resp.message(crypto(user_parameter))
        return str(resp)
    elif key_command == "directions":
        resp.message(directions(user_parameter, message_body[2]))
        return str(resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
