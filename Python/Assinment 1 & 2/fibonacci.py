
def fibonacci(num):
    first = 0
    second = 1
    print(first)
    print(second)
    while(num>0):
        sum = first + second
        first = second
        second = sum
        print(sum)
        num -= 1

num = int(input("Enter number: "))

fibonacci(num)
        
