def main():
    print("We meet again heckor ,this time in py.Are you sure you wanna challenge me?")
    ch=input()
    if 'y' in ch:
        start()
    else:
        print("gud boi")
def start():
    print("YARE YARE DAZE")#watch jojo's bizarre adventure
    print("try to enter this safe")
    print("give the code")
    code=int(input())
    vault(code)

def vault(code):
    code1=(((code>>4)^1234)*(1000^code))+11111111
    code2=(((code<<4)^4321)*(1^code))+1337
    code3=code2*code1
    code=code3^(code1+code2)
    if code == 319637485806547726208542445724320951469370207:
        print_flag()

def check_key(key):
    if ((key**2)^12345)>>4!=732261981515316393:
        print("Atlast i defeated you V ,Oh you are not V.that's why i thought how V can be this weak")
        exit()


def print_flag():
    print("you thought i will let you go so easily,V")
    print("give me key:")
    key=int(input())
    check_key(key)
    print("Oh nice.you are a good man.let's team up next time")
    f = open("flag.txt", "r")
    print(f.read())

if __name__ == "__main__": 
    main()
