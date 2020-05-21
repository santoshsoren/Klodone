
class Student:
    def __init__(self,name):
        self.name = name

    def st_name(self):
        return name

class Department:
    def __init__(self,dept):
        self.dept = dept

    def st_dept(self):
        return dept

class Graduation(Student,Department):
    def __init__(self,name,dept,passing_year):
        Student.__init__(self,name)
        Department.__init__(self,dept)
        self.passing_year = passing_year

    def detail(self):
        print(self.name)
        print(self.dept)
        print(self.passing_year)

name = input("Enter student name: ")
department = input("Enter student department: ")
pass_year = int(input("Enter graduation year: "))

grd = Graduation(name,department,pass_year)

grd.detail()
