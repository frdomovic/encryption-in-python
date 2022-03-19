from Crypto.Hash import HMAC, SHA256

secret = b'Kockavica'
h = HMAC.new(secret, digestmod=SHA256)
print(h.hexdigest())

#validation of msg 
secret = b'Kockavica'
h2 = HMAC.new(secret, digestmod=SHA256)

try:
    h.hexverify(h2.hexdigest())
    print("The message '%s' is authentic" %'Dobrovece')
except ValueError:
    print("The message or the key is wrong")
