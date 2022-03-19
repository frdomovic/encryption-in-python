#!/usr/bin/env python3
import sys
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

if(sys.argv[1] == 'init'):
    password = str.encode(sys.argv[2])
    salt = get_random_bytes(16)

    derivatedKey = PBKDF2(password, salt, 16, count=1000000, hmac_hash_module=SHA512)
    cipher = AES.new(derivatedKey, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(b'username-password')
    with open("encrypted.txt","wb") as f:
        [f.write(x) for x in (cipher.nonce, tag,salt, ciphertext)]
    print('Password manager initialized.')

elif(sys.argv[1] == 'get'):
    pwd = str.encode(sys.argv[2])
    usr = sys.argv[3]
    with open('encrypted.txt', 'rb') as f:
        nonce, tag, salt, ciphertext = [ f.read(x) for x in (16, 16,16, -1) ]
        derivatedKey = PBKDF2(pwd, salt, 16, count=1000000, hmac_hash_module=SHA512)
        cipher = AES.new(derivatedKey, AES.MODE_GCM, nonce)
        try:
            data = cipher.decrypt_and_verify(ciphertext, tag)
            userdata = data.decode('utf-8').split('-')
            if(userdata[0] == usr):
                print("Password for "+userdata[0]+" is : "+userdata[1])
            else:
                print("Username not saved!")
            
        except ValueError:
            print("Wrong master password or message corrupted!")
    
elif(sys.argv[1] == 'put'):
    pwd = str.encode(sys.argv[2])
    usr = (sys.argv[3])
    usrpwd =(sys.argv[4])
     
    with open('encrypted.txt', 'rb') as f:
        nonce, tag, salt, ciphertext = [ f.read(x) for x in (16, 16,16, -1) ]
        derivatedKey = PBKDF2(pwd, salt, 16, count=1000000, hmac_hash_module=SHA512)
        cipher = AES.new(derivatedKey, AES.MODE_GCM, nonce)
        try:
            data = cipher.decrypt_and_verify(ciphertext, tag)
        except ValueError:
            print("Wrong master password or message corrupted!")
    salt = get_random_bytes(16)
    derivatedKey = PBKDF2(pwd, salt, 16, count=1000000, hmac_hash_module=SHA512)
    cipher = AES.new(derivatedKey, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(str.encode(usr+"-"+usrpwd))
    with open("encrypted.txt","wb") as f:
        [f.write(x) for x in (cipher.nonce, tag,salt, ciphertext)]
    print('Password for '+usr+' stored!')
else:
    print("command not found, try again! (available commands: init , get ,put )") 
