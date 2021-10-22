<h1 align="center">GeoSMS</h1>

<p align="center">
  <img alt="badge-lastcommit" src="https://img.shields.io/github/last-commit/utkm/GeoSMS?style=for-the-badge">
  <img alt="badge-openissues" src="https://img.shields.io/github/issues-raw/utkm/GeoSMS?style=for-the-badge">
  <img alt="badge-license" src="https://img.shields.io/github/license/utkm/GeoSMS?style=for-the-badge">
  <img alt="badge-contributors" src="https://img.shields.io/github/contributors/utkm/GeoSMS?style=for-the-badge">
  <img alt="badge-codesize" src="https://img.shields.io/github/languages/code-size/utkm/GeoSMS?style=for-the-badge">
</p>

<p align"center">
  <img alt="GeoSMS-logo" src="https://user-images.githubusercontent.com/46727048/138494065-30dc6a72-b86d-46ac-8803-d0fecc0f0048.png" />
</p>

## What is GeoSMS?

### Inspiration
In lots of places in the world, the Internet does not arrive due to the lack of infrastructure, leaving people in these areas disconnected. This is a big problem because it disallows them to access many important facilities in our present world. Still, the coverage area of SMS tends to be larger than the area of Internet coverage. That's why we came with the idea of GeoSMS. GeoSMS allows these people to perform some operations that they wouldn't be able to perform otherwise.

Additionally, GeoSMS can also be useful in urban areas. After all, have you ever been stuck in some sort of an emergency situation like being lost when you have no Wi-Fi and no data? Actually, I have been, and trust me when I say that it's not fun. To solve this, GeoSMS allows you to perform various emergency searches such as finding the directions to an address, which supports directions via transit data, and then we also added some mini-games to lighten up your mood while you wait.

### How it works? 🤔
First, the user sends an SMS text message to the Twilio number (currently, the number has to be authorized to be able to do this). Then, the backend arrives to the server which processes your request. Once processed, the backend will send a reply through another SMS text message with the corresponding reply for your request. Finally, the user receives the SMS text message with his message.

The server can process lots of different operations such as searching something on Google, defining words, finding directions or getting information about busses. There are also some fun options like being told a joke or generating a random piece of advice.

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
