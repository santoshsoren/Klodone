
class Square:
    def __init__(self,length):
        self.length = length

    def area_square(self):
        print("Area of Square: ",self.length**2)

class Rectangle(Square):
    def __init__(self,length,breadth):
        Square.__init__(self,length)
        self.breadth = breadth

    def area_rectangle(self):
        print("Area of Rectangle: ",self.length*self.breadth)

class cuboid(Rectangle):
    def __init__(self,length,breadth,height):
        Rectangle.__init__(self,length,breadth)
        self.height = height

    def area_cuboid(self):
        print("Area of Cuboid: ",self.length*self.breadth*self.height)

a = int(input("Enter length: "))
b = int(input("Enter breadth: "))
c = int(input("Enter height: "))

area = cuboid(a,b,c)
area.area_cuboid()
area.area_rectangle()
area.area_square()
