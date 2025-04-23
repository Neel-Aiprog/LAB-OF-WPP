class Shape:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

class Rectangle(Shape):
    def area1(self, l, b):
        return  l * b

    def perimeter1(self, l, b):
        return 2 * (l + b)

class Circle(Shape):
    def area2(self, r):
        return 3.14 * r * r

    def perimeter2(self, r):
        return 2 * 3.14 * r

c = Rectangle()
print(c.area1(2, 4))
d=Circle()
print(d.area2(3))  
