# A Project Made For Hack the North 2021!
Inspiration 💡 <br />
<br />
Have you ever been stuck in some sort of an emergency situation like being lost when you have no wifi and no data, funny enough, I actually have an trust me, it’s not fun. To solve this, we created GeoSMS, an SMS service that allows you to perform various emergency searches such as finding the directions to an address, which supports directions via transit data, and then we also added some mini-games to lighten up your mood while you wait.

What it does 🤔 <br />
<br />
First, send an SMS to the Twilio number (your number has to be authorized to be able to do this) which should include a command term. Then you will receive a reply for your request. This can be really helpful if you need directions to a certain address but don't have Wifi, or if you would like to take the bus but don't know which one to take. Other than those fundamental features, there are mini-games (like defining a word, being told a joke, generating a random piece of advice, searching google while being offline, and checking a cryptocurrency) you can play while you wait.

Quick start 🚀 <br />
<br />
1. Connect the flask server-side from your local host to ngrok(do not change port number) you can find info about ngrok here https://ngrok.com/
2. Input all the necassary API Keys for the various providers used in the features.py file
3. Make sure to have twilio set up with a number to use for receiving and sending SMS texts back to the client
4. Launch app.py and start invoking commands by sending them to the number you have assigned on twilio and app.py as the number that will send and receive messages from and back to the client.
5. Commands should start returning responses!
6. Thats all!😄
