
def pattern_1(num):
    for i in range(num):
        for j in range(num-i):
            print("*",end="")
        print("\r")

n = int(input("Enter number: "))
pattern_1(n)
