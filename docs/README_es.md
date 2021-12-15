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

# Traducciones
- [English](https://github.com/utkm/GeoSMS/blob/main/docs/README.md).
- [Español](https://github.com/utkm/GeoSMS/blob/main/docs/README_es.md) (Leyendo esta ahora).

## ¿Qué es GeoSMS?

### Inspiración
En muchas partes del mundo, el internet no llega debido a la falta de infrastructura, dejando a las personas en estas áreas desconectadas. Esto es un gran problema porque no les permite acceder a muchos servicios importantes en nuestro mundo actual. Aún así, el área de cobertura de los Servicios de Mensajes Cortos (SMS por sus siglas en inglés "Short Messages Service"). Es por ello que se tuvimos la idea de GeoSMS. GeoSMS les permite a esas personas realizar algunas operaciones que no podrían hacer de otra forma.

Adicionalmente, GeoSMS también puede ser útil en las áreas urbanas. ¿Después de todo, no te ha sucedido alguna vez que te encuentras en algún tipo de emergencia como estar perdido sin Wi-Fi y sin datos? De hecho, yo lo he estado, y créeme cuando te digo que no es divertido. Para solucionar esto, GeoSMS te permite realizar varias búsquedas de emergencia como buscar instrucciones para llegar a un lugar y también tiene algunos juegos para eleverte el ánimo mientras esperas.

### ¿Cómo funciona? 🤔

Primero, el usuario envía un mensaje SMS a un número de Twilio (actualmente, el número debe estar autorizado para poder hacer esto). Después, el _backend_ recibe el mensaje y procesa la petición. Una vez hecho esto, el _backend_ enviará una respuesta a través de otro mensaje SMS con la respuesta correspondiente a tu petición. Finalmente, el usuario recibe el mensaje SMS con su mensaje.

El servidor puede procesar montones de operaciones diferentes como buscar en Google, definir palabras, buscar direcciones u obtener información de buses. También hay algunas opciones para divertirse como contar un chiste o generar un consejo aleatorio.

### Instalación rápida 🚀
1.Conéctate desde el _backend_ flask de tu _localhost_ a "ngrok" (no cambies el número de puerto). Puedes encontrar información de "ngrok" [aquí](https://ngrok.com/) (La página se encuentra en idioma inglés).
2. Inserta todals las llaves de las Interfaces de Programación de Aplicaciones (API por sus siglas en inglés, "Application Programming Interface") de los diferentes proveedores en el archivo `features.py`.
3. Asegúrate que tienes Twilio configura con un número para recibir y enviar mensajes al cliente.
4. Corre `app.py` y empieza a invocar comandos enviándolos al número que elegiste en Twilio y en `app.py` para enviar y recibir mensajes del y al cliente.
5. Mira las respuestas que devuelve.

Eso es todo!😄

### Demonstración (Está en idioma inglés)

https://user-images.githubusercontent.com/45953426/138011988-47ea907d-def0-4344-bd57-177c60ed9c55.MP4

## Licencia
Todo el código poseído en este repositorio está bajo la licencia del [MIT](https://github.com/utkm/GeoSMS/blob/main/LICENSE) (El documento se encuentra en idioma inglés).

## Contribuidores
¡Gracias a todas estas personas maravillosas por permitir que GeoSMS sea posible!

<p align="center"><a href="https://github.com/utkm/GeoSMS/graphs/contributors"><img src="https://contrib.rocks/image?repo=utkm/GeoSMS" /></a></p>
