# this progrma calculates BMI
from colorama import Fore

name = input("Enter Your name : ")
heightCM = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))

def bmiCal(weight, height) :
    heightM = (height / 100) ** 2
    bmi = weight / heightM
    print(name + ", your BMI is {:.2f}".format(bmi))

    if bmi < 18.5 :
        print("\n"+Fore.YELLOW,name + ", You are Underweight")
    elif bmi < 24.9 :
        print("\n"+Fore.GREEN, name + ", You are Normal")
    elif bmi < 29.9 :
        print("\n"+Fore.RED, name + ", You are Overweight")
    else:
        print("\n"+Fore.LIGHTRED_EX,name + ", You are obese")

bmiCal(weight, heightCM)