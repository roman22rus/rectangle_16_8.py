class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self,x):
        self.x = x
    def get_area_square(self):
        return self.x ** 2
class Circle:
    def __init__(self,r):
        self.r = r
    def get_area_circle(self):
        return 3.14*self.r **2
