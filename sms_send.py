import os
import rsa
import clx.xms.client
from dotenv import load_dotenv
import base64

load_dotenv()

with open("bob_pub.pem", mode="rb") as privatefile:
    keydata = privatefile.read()
bob_pub = rsa.PublicKey.load_pkcs1_openssl_pem(keydata)

message = "Hello Bob!".encode("utf8")
crypto = rsa.encrypt(message, bob_pub)

print("Plaintext:           ", message)
print("Cyphertext:          ", crypto)

service_plan_id = os.environ["SERVICE_PLAN_ID"]
token = os.environ["TOKEN"]

client = clx.xms.Client(service_plan_id, token)

# Base64 encryption
body = base64.b64encode(crypto)
# A string must be sent, so we decode the Bytes to a String
body = body.decode(encoding="utf8")

print("Message sent:       ", body)

client.create_text_message(sender="+12029671765", recipient="+19726274086", body=body)
