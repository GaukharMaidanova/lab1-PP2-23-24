class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self)
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width

x = int(input())
y = int(input())
a = Rectangle(x, y)
print(a.area())  