from binascii import unhexlify 
import hashlib
import numpy as np
from Crypto.Util.number import getPrime, long_to_bytes

Cip= "74fe2c74897b3553dd91af6ade54bb91d93bc3f1c082cff76d08db5527047fdd"
Sol= "323731373630343234383437383a323838393530353630363233363a333539323039383439393134363a"
Add= "37363438323a38303635303a39313535303a39353730363a39313231383a37393137363a39383235383a39393635363a3133303633323a"

ci=unhexlify(Cip).encode('utf-8')
so=unhexlify(Sol).encode('utf-8')
ad=unhexlify(Add).encode('utf-8')

gen_mtx=lambda size,x,y: [[getPrime(size)for j in range(x)]for i in range(y)]
gen_byt=lambda mat,x,y: "".join([str(mat[j,i])+":" for j in range(y) for i in range(x)]).encode('utf-8')
xor = lambda x, y: b''.join([bytes([i^j]) for i,j in zip(x, y)])
x = np.matrix(gen_mtx(24,1,3))

key=gen_byt(x,1,3)

hash_key=hashlib.sha256(key).hexdigest()

plain=xor(ci, bytes.fromhex(hash_key))

print(plain)
