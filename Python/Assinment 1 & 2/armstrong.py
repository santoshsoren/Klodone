
def armstrong(num):
    sum = 0
    temp = num
    while(num>0):
        r = num%10
        sum +=r**3 
        num //= 10
    if(temp==sum):
        print("armstrong number")
    else:
        print("not armstrong")

n = int(input("enter the number: "))
armstrong(n)
