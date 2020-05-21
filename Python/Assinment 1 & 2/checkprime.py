
def check_prime(num):
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
    else:
        print("prime")

n = int(input("Enter number: "))
check_prime(n)
