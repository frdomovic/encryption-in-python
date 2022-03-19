#!/usr/bin/env python3
import sys
from Crypto.Cipher import Salsa20
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC, SHA256

if(sys.argv[1] == 'init'):
    password = str.encode(sys.argv[2])
    salt = get_random_bytes(16)
    key = scrypt(password, salt, 16, N=2**14, r=8, p=1)
    print("key is ", key)
    
    cipher = Salsa20.new(key)
    print("nonce is ", cipher.nonce)
    
    #kriptiramo masterpassword
    ciphertext = cipher.encrypt(key)
    with open('test.txt', 'wb') as f:
        f.write(ciphertext)
        

    

    
elif(sys.argv[1] == 'put'):
    print("put")
elif(sys.argv[1] == 'get'):
    with open('test.txt', 'rb') as f:
        data = f.readlines()
        for line in data:
            print(line)
        #cipher = Salsa20.new(key=mk, nonce=kn)
        #print(cipher.decrypt(ciphertext))
        
else:
    print("error: wrong command!")
