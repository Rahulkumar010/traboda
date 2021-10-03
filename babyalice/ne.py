from Crypto.Util.number import *
from Crypto.PublicKey import RSA

f = open('publickey1.pem').read()
n = RSA.importKey(f).n
e = RSA.importKey(f).e

print('n: ',n)
print('e: ',e)

f2 = open('publickey2.pem').read()
n2 = RSA.importKey(f2).n
e2 = RSA.importKey(f2).e

print('n2: ',n2)
print('e2: ',e2)

