<h1 align="center">GeoSMS</h1>

## What is GeosMS?

### Inspiration
Have you ever been stuck in some sort of an emergency situation like being lost when you have no Wi-Fi and no data. Actually, I have been, and trust me. It’s not fun. To solve this, we created GeoSMS, an SMS service that allows you to perform various emergency searches such as finding the directions to an address, which supports directions via transit data, and then we also added some mini-games to lighten up your mood while you wait.

### How it works? 🤔
First, send an SMS to the Twilio number (currently your number has to be authorized to be able to do this) which should include a command term. Then, you will receive a reply for your request. This can be really helpful if you need directions to a certain address but don't have Wi-fi, or if you would like to take the bus but don't know which one to take. Other than those fundamental features, there are mini-games (like defining a word, being told a joke, generating a random piece of advice, searching google while being offline, and checking a cryptocurrency) you can play while you wait.<br />

### Quick start 🚀
1. Connect the flask server-side from your localhost to "ngrok" (do not change port number). You can find info about "ngrok" [here](https://ngrok.com/).
2. Input all the necessary API leys for the various providers used in the `features.py` file.
3. Make sure to have Twilio set up with a number for receiving and sending SMS texts messages back to the client.
4. Launch` app.py` and start invoking commands by sending them to the number you have assigned on Twilio and `app.py` as the number that will send and receive messages from and back to the client.
5. Look at the returning responses!

Thats it!😄

### Demonstration

https://user-images.githubusercontent.com/45953426/138011988-47ea907d-def0-4344-bd57-177c60ed9c55.MP4
