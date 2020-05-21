
def addition(num1,num2):
    sum = num1+num2
    print(sum)

def subtraction(num1,num2):
    sub = num1-num2
    print(sub)

def multiplication(num1,num2):
    mul = num1*num2
    print(mul)

def division(num1,num2):
    div = num1/num2
    print(div)

print("Select option: \n"
      "1. addition\n"\
      "2. subtraction\n"\
      "3. multiplication\n"\
      "4. division\n")

option = int(input("Select option: "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def operation(num1,num2):
    if option == 1:
        print("addition: ")
        addition(num1,num2)
    elif option == 2:
        print("subtraction: ")
        subtraction(num1,num2)
    elif option == 3:
        print("multiplication: ")
        multiplication(num1,num2)
    elif option == 4:
        print("division: ")
        division(num1,num2)
    else:
        print("invalid option")

operation(num1,num2)
    
