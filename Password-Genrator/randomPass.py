# this Program Generatre random and strong pass 
import random
from re import U

while True:
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXVZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    sysmb = '!^#$%&()?*.@'

    string = upper + lower + num + sysmb 
    len = int(input("Enter Length : "))
    password = "".join(random.sample(string, len-1))

    print("Your password is : {}" + password)

    genAgain = input("You want to genrate password again (y/n) : ")
    if genAgain.lower() == 'n':
        break
