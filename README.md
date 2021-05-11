# .env
Crear un archivo .env que contenga las variables mostradas en .env.example utilizando los valores proporcionados por @AndresBeriss

# Flask
Para iniciar el servidor de Flask primero hace falta definir la variable de entorno FLASK_APP

En PowerShell:

`$env:FLASK_APP = "sms_receive.py"`

Para iniciar el servidor

`flask run`

# ngrok
Crear una cuenta en ngrok.com y obtener tu authtoken

Correr

`./ngrok authtoken [authtoken]`

`./ngrok http 5000`

Y copia la forwarding address generada

# Twilio
Navega a la sección de Phone Numbers -> Active Numbers y haz click en tu número activo.

En la sección de Messaging, pega la dirección generada por ngrok en el campo de "A Message Comes In"

# Envío de SMS
Configurar los parámetros adecuados de sender y recipient en la función `create_text_message`.