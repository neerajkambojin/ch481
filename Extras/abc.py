import math


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area is ", math.pi*self.r*self.r)

    def circum(self):
        print(f"Circumference is {2*math.pi*self.r}")

circle1 = Circle(45)

circle1.area()
circle1.circum()
