
class candidate:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def st_name(self):
        return self.name

    def st_age(self):
        return self.age

class details(candidate):
    def __init__(self,name,age):
        candidate.__init__(self,name,age)

    def voter(self):
        if age >= 18:
            print(self.name)
            print(self.age)
            print("You are eligible for voting.")
        else:
            print(self.name)
            print(self.age)
            print("You are not eligible for voting.")

name = input("Enter candidate name: ")
age = int(input("Enter candidate age: "))

d1 = details(name,age)

d1.voter()
