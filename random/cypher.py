#!/usr/bin/env python3
from Crypto.Cipher import Salsa20

key = b'0123456789012345'
cipher = Salsa20.new(key)
ciphertext = cipher.encrypt(b'Moja tajna poruka')
ciphertext += cipher.encrypt(b' Druga poruka')
print(ciphertext)
cipher = Salsa20.new(key=key, nonce=cipher.nonce)
print(cipher.decrypt(ciphertext))