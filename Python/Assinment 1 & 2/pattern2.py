
def pattern2(num):
    k = 2*n-1
    for i in range(num):
        for j in range(k):
            print(end=" ")
        k = k-1
        for j in range(i+1):
            print("*",end="")
        print("\r")

n = int(input("Enter number: "))
pattern2(n)
