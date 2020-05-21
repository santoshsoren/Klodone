
def swap(num1, num2):
    print("Before swapping: ",num1,num2)
    temp = num1
    num1= num2
    num2 = temp
    print("After swapping: ",num1,num2)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

swap(n1,n2)
