import os
from rsa import encrypt
import clx.xms.client
from dotenv import load_dotenv
import base64

load_dotenv()

message = "Hello Bob!"

public_key = {}
with open("bob_pub.pem") as f:
    for line in f:
        (n, e) = line.split()
    public_key["n"] = int(n)
    public_key["e"] = int(e)

ciphertext = encrypt(message, public_key)

print("Plaintext:           ", message)
print("Cyphertext:          ", ciphertext)

service_plan_id = os.environ["SERVICE_PLAN_ID"]
token = os.environ["TOKEN"]

client = clx.xms.Client(service_plan_id, token)

client.create_text_message(
    sender="+12029671765", recipient="+19726274086", body=ciphertext
)
