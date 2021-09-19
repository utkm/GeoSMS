import json
from flask import Flask, request
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# User defined variables
number = request.form['From']
message_body = request.form['Body']

@app.route('/')
def home():
    return "Hello"


@app.route('/transitapi', methods = ['POST', 'GET'])
def transitprocess():
    jsondata = request.get_json()
    data = json.loads(jsondata)

    if data['BUSID'] == '123':
        result = {
            'Bus Stop':'example: 15 Minutes Away'
        }
        return json.dumps(result)


@app.route('/sms', methods=['POST'])
def sms():
    resp = MessagingResponse()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)