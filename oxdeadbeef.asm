extern printf
extern scanf

section .data
        fmt: db "%ld",0
        output: db "Correct",10,0
        out: db "Not Correct",10,0
        inp1: db "Input 1st number:",0
        inp2: db "Input 2nd number:",0

section .text
        global main
 
        main:
        push ebp
        mov ebp,esp
        sub esp,0x10
 
        push inp1
        call printf
        lea eax,[ebp-0x4]
        push eax
        push fmt
        call scanf

        push inp2
        call printf
        lea eax,[ebp-0xc]
        push eax
        push fmt
        call scanf

        mov ebx, DWORD[ebp-0xc]
        add ebx, DWORD[ebp-0x4]
        cmp ebx,0xdeadbeef
        jne N

        cmp DWORD[ebp-0x4], 0x6f56df65
        jg N

        cmp DWORD[ebp-0xc], 0x6f56df8d
        jg N
        cmp DWORD[ebp-0xc], 0x6f56df8d
        jl N
        jmp O

        N:
        push out
        call printf
        leave
        ret

        O:
        push output
        call printf

        leave
        ret
