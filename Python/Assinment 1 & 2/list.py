
def list(num):
    print("Length of list: ",len(num))
    print(type(num))
    print(num)
    print(num[2:5])
    print(num[4])
    num[1] = 10
    print(num)
    num.append(13)
    print(num)
    num.remove(6)
    print(num)
    del num[0]
    print(num)
    num.sort()
    print(num)
    num.reverse()
    print(num)
    st = ["iphone","samsung","xiomi"]
    num.extend(st)
    print(num)
    num.insert(2,6)
    print(num)

num = [5,7,8,6,9,11,2]
list(num)
