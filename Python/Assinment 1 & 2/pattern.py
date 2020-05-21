
def pattern(num):
    for i in range(num):
        for j in range(i+1):
            print("*",end="")
        print("\r")

n = int(input("Enter number: "))
pattern(n)
