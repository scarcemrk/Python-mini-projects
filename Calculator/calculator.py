# This program do sipmle mathamatical calculation (Addition, Subtraction, Multiplication, Division, Modulo, Power)

# Function for diffrent operation
def addtion(num1, num2):
    print("\nAddition of two number is ",num1+num2)

def subtraction(num1, num2):
    print("\nSubtraction of two number is ",num1-num2)
def multiplication(num1, num2):
    print("\nMultiplication of two number is ",num1*num2)

def division(num1, num2):
    print("\nDivision of two number is ",num1/num2)

def modulo(num1, num2):
    print("\nModulo of two number is ",num1%num2)

def power(num1, num2):
    print("\nPower of two number is ",num1**num2)

print("Operation menu \n1. Addition of two number\n2. Subtraction of two number\n3. Multiplication of two number\n4. Division of two number\n5. Modulo of two number\n6. Power of two number\n")

# Get User input
choice = int(input("Enter operation (1, 2, 3, 4, 5, 6) : "))

num_one = float(input("Enter first number : "))
num_two = float(input("Enter second number : "))



# Check condition and do calculation 
if choice == 1: # if user choose opetion no.1 (Addition)
    addtion(num_one,num_two)

elif choice == 2: # if user choose opetion no.2 (Subtraction)
    subtraction(num_one,num_two)

elif choice == 3: # if user choose opetion no.3 (Multiplication)
    multiplication(num_one,num_two)

elif choice == 4: # if user choose opetion no.4 (Division)
    division(num_one,num_two)

elif choice == 5: # if user choose opetion no.5 (Modulo)
    modulo(num_one,num_two)

elif choice == 6: # if user choose opetion no.6 (Power)
    power(num_one,num_two)

else : # if user enter any other choice (Invalid Choice)
    print("Invalid Operation :(")
