<h1 align="center">GeoSMS</h1>

<p align="center">
  <img alt="badge-lastcommit" src="https://img.shields.io/github/last-commit/utkm/GeoSMS?style=for-the-badge">
  <img alt="badge-openissues" src="https://img.shields.io/github/issues-raw/utkm/GeoSMS?style=for-the-badge">
  <img alt="badge-license" src="https://img.shields.io/github/license/utkm/GeoSMS?style=for-the-badge">
  <img alt="badge-contributors" src="https://img.shields.io/github/contributors/utkm/GeoSMS?style=for-the-badge">
  <img alt="badge-codesize" src="https://img.shields.io/github/languages/code-size/utkm/GeoSMS?style=for-the-badge">
</p>

<p align"center">
  <img alt="GeoSMS-logo" src="https://user-images.githubusercontent.com/46727048/138491522-f7afea69-3034-4b7d-8182-5bf4e2049ccc.jpeg" />
</p>

## What is GeoSMS?

### Inspiration
Have you ever been stuck in some sort of an emergency situation like being lost when you have no Wi-Fi and no data? Actually, I have been, and trust me. It’s not fun. To solve this, we created GeoSMS, an SMS service that allows you to perform various emergency searches such as finding the directions to an address, which supports directions via transit data, and then we also added some mini-games to lighten up your mood while you wait.

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

## License
All the code owned in this repository is under the [MIT license](https://github.com/utkm/GeoSMS/blob/main/LICENSE).

## Contributors
Thanks to these wonderful people for making GeoSMS possible!

<p align="center"><a href="https://github.com/utkm/GeoSMS/graphs/contributors"><img src="https://contrib.rocks/image?repo=utkm/GeoSMS" /></a></p>
