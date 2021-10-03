#!/usr/bin/python3

import numpy as np
import hashlib 
from Crypto.Util.number import getPrime, long_to_bytes
from binascii import hexlify
from key import Flag

gen_mtx=lambda size,x,y: [[getPrime(size)for j in range(x)]for i in range(y)]
gen_byt=lambda mat,x,y: "".join([str(mat[j,i])+":" for j in range(y) for i in range(x)]).encode('utf-8')
xor = lambda x, y: b''.join([bytes([i^j]) for i,j in zip(x, y)])

def gen_key():
	x = np.matrix(gen_mtx(24,1,3))
	A = np.matrix(gen_mtx(16,3,3))
	B = np.matrix(gen_mtx(16,3,3))
	C = (A*x)+(B*x)
	return gen_byt(x,1,3), gen_byt(C,1,3),gen_byt(A+B,3,3)

def main():
	key, sol, add = gen_key()
	hashed_key = hashlib.sha256(key).hexdigest()
	cip = xor(Flag, bytes.fromhex(hashed_key))

	with open("../Handout/encryption.txt","w") as e:
		e.truncate(0)
		e.write("Cip: "+hexlify(cip).decode('utf-8')+'\n')
		e.write("Sol: "+hexlify(sol).decode('utf-8')+'\n')
		e.write("Add: "+hexlify(add).decode('utf-8')+'\n')

if __name__ == '__main__':
	main()