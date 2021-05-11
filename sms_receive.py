import rsa
import base64
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

with open("bob_priv.pem", mode="rb") as privatefile:
    keydata = privatefile.read()
bob_priv = rsa.PrivateKey.load_pkcs1(keydata)


@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    # Get the message the user sent our Twilio number
    body = request.values.get("Body", None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("\nMessage sent: " + body)

    print("\nMessage received:\n" + body + "\n")

    return str(resp)


@app.route("/decrypt", methods=["GET", "POST"])
def sms_decrypt():
    # Get the message the user sent our Twilio number
    body_string = request.values.get("Body", None)
    # Convert String back to Bytes
    body = body_string.encode(encoding="utf8")
    # Decode the Base64 encryption
    body = base64.b64decode(body)
    # RSA decryption
    message = rsa.decrypt(body, bob_priv)

    # Start our TwiML response
    resp = MessagingResponse()

    print("\nMessage received:")
    print(body_string)

    print("\nDecrypted message:")
    print(message, end="\n\n")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
