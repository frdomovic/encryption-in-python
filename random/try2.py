#!/usr/bin/env python3
import sys
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC, SHA256

if(sys.argv[1] == 'init'):

    password = str.encode(sys.argv[2])

    h = HMAC.new(password, digestmod=SHA256)
    hashedKey = h.hexdigest()
    #print(hashedKey)
    print(str.encode(hashedKey))
    with open('test.txt', 'wb') as f:
        f.write(str.encode(hashedKey))
elif(sys.argv[1] == 'get'):
    password = str.encode(sys.argv[2])
    h = HMAC.new(password, digestmod=SHA256)
    hashedKey = h.hexdigest()
    with open('test.txt', 'rb') as f:
        data = f.readline()
        try:
            h.hexverify(data)
            print("The key is ok")
        except ValueError:
            print("The message or the key is wrong")
        