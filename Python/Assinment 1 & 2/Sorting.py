
def Sorting(num):
    n = len(num)
    for i in range(n):
        for j in range(0,n-i-1):
            if num[j]>num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp

    for i in range(len(num)):
        print(num[i])
                

num = [8,7,5,6,2,4,9,3]
Sorting(num)

                
                
            
