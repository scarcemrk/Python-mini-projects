# this Program Generatre random and strong pass 
import random
from colorama import Fore

while True:
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXVZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    sysmb = '!^#$%&()?*.@'

    string = upper + lower + num + sysmb 
    len = int(input("[+] Enter Length : "))
    password = "".join(random.sample(string, len))

    print("[=] Your password is : "+Fore.RED + password)

    genAgain = input(Fore.WHITE+"\n[+] You want to genrate password again (y/n) : ")
    if genAgain.lower() == 'n':
        break
