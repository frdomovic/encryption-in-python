import sys
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

key = b'password12345dwadwdawwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
salt = get_random_bytes(32)
keys = PBKDF2(key, salt, 64, count=1000000, hmac_hash_module=SHA512)
keyz = keys[:32]
print(len(keyz))
cipher = AES.new(keyz, AES.MODE_GCM)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(b'Kriptiranje necega bitnog')


cipher2 = AES.new(keyz, AES.MODE_GCM, nonce=nonce)
plaintext = cipher2.decrypt(ciphertext)
print(plaintext.decode("utf-8"))
# # try:
# #     cipher2.verify(tag)
    
# #     print("Message is authentic:", plaintext)
# # except ValueError:
# #     print("Incorrect key or message corrupted")