
def reverse(strg):
    str = ""
    for i in strg:
        str = i+str
    return str

st = input("Enter string: ")
print(reverse(st))
