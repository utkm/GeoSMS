import sys
import json
import requests

conv = {'BUSID': '123'}
s = json.dumps(conv)
res = requests.post("https://37c8-70-31-154-23.ngrok.io//transitapi", json=s).json()
print(res['Bus Stop'])