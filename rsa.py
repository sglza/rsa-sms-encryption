import sympy
import numpy as np
import os


def gdc(a, b):

    if a == 0:
        return b
    else:
        return gdc(b % a, a)


def get_prime():
    return sympy.randprime(1000000, 2000000)


def get_phi(p, q):
    return (p - 1) * (q - 1)


def get_e(phi):
    e = 2

    while e < phi:
        if gdc(e, phi) == 1:
            break

        e += 1

    return e


def generate_public_key(p, q):
    public_key = {}

    n = p * q
    public_key["n"] = n

    phi = get_phi(p, q)
    e = get_e(phi)
    public_key["e"] = e

    return public_key


def generate_private_key(p, q):
    phi = get_phi(p, q)
    e = get_e(phi)
    n = p * q
    d = 0

    for i in range(9):
        x = 1 + (i * phi)

        if x % e == 0:
            d = x / e

    private_key = {"n": n, "d": int(d)}

    return private_key


def encrypt(message, public_key):

    n = public_key["n"]
    e = public_key["e"]

    messages_numbers = [ord(c) for c in message]

    print("Plaintext in ASCII:   " + " ".join(str(n) for n in messages_numbers))

    ciphertext = []

    for number in messages_numbers:
        cipherletter = pow(number, e, n)
        ciphertext.append(cipherletter)

    ciphertext = " ".join(str(n) for n in ciphertext)

    return ciphertext


def decrypt(ciphertext, private_key):

    ciphertext = ciphertext.split()
    ciphertext = [int(n) for n in ciphertext]

    n = private_key["n"]
    d = private_key["d"]

    plaintext = []

    for cipherletter in ciphertext:
        plainletter = pow(cipherletter, d, n)
        plaintext.append(plainletter)

    print("Decrypted message in ASCII:\n" + " ".join(str(n) for n in plaintext))

    plaintext = "".join(chr(n) for n in plaintext)

    return plaintext


def rsa(message):

    p = get_prime()
    q = get_prime()

    public_key = generate_public_key(p, q)
    private_key = generate_private_key(p, q)

    print("\nPublic key: " + str(public_key))
    print("Private key: " + str(private_key))

    print("\n----------Encryption----------")

    ciphertext = encrypt(message, public_key)
    print("Ciphertext: " + str(ciphertext))

    print("\n----------Decryption----------")

    plaintext = decrypt(ciphertext, private_key)
    print("Plaintext: " + str(plaintext))
