import numpy as np

list1 = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]

print(np.matrix(list1))

def position(x,y,n):
    for i in range(9):
        if list1[x][i] == n:
            return False
    for i in range(9):
        if list1[i][y] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if list1[x0+i][y0+j] == n:
                return False
    return True

def solution():
    for x in range(9):
        for y in range(9):
            if list1[x][y] == 0:
                for n in range(1,10):
                    if position(x,y,n):
                        list1[x][y] = n
                        solution()
                        list1[x][y] = 0
                return
    print("The solution is here: ")
    print(np.matrix(list1))
    

solution()
