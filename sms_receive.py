import os
import base64
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from rsa import get_prime, generate_private_key, generate_public_key, decrypt

app = Flask(__name__)

p = get_prime()
q = get_prime()

bob_pub = generate_public_key(p, q)
bob_priv = generate_private_key(p, q)

f = open("bob_pub.pem", "w")
f.write(str(bob_pub["n"]) + " " + str(bob_pub["e"]))
f.close()


@app.route("/decrypt", methods=["GET", "POST"])
def sms_decrypt():
    # Get the message the user sent our Twilio number
    body = request.values.get("Body", None)
    # RSA decryption
    message = decrypt(body, bob_priv)

    # Start our TwiML response
    resp = MessagingResponse()

    print("\nMessage received:")
    print(body)

    print("\nDecrypted message:")
    print(message, end="\n\n")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
