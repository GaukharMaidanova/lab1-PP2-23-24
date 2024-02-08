import math
class MyShape(object):
    def __init__(self, color = "green", is_filled = False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"
    
    def getArea(self):
        return 0
    
class Rectangle(MyShape):
    def __init__(self, color, is_filled, x_top_left, y_top_left, length, width):
        super().__init__(color, is_filled)
        MyShape.__init__(self)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length*self.width
    
    def __str__(self):
        return f"Rectangle: {self.x_top_left=}, {self.y_top_left=}, Length: {self.length}, Width: {self.width}, {super().__str__()}"
    

class Circle(MyShape):
    def __init__(self, color, is_filled, x_center, y_center, radius):
        super().__init__(color, is_filled)
        MyShape.__init__(self)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return math.pi*math.pow(self.radius, 2)
    
    def __str__(self):
        return f"Circle: {self.x_center=}, {self.y_center=}, Radius: {self.radius}, {super().__str__()}"
    
def create_rectangle():
    color = input("Enter color: ")
    is_filled = input("Is filled?: ").lower() == 'true'
    x_top_left = float(input("Enter x coordinate of top left corner: "))
    y_top_left = float(input("Enter y coordinate of top left corner: "))
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    return Rectangle(color, is_filled, x_top_left, y_top_left, length, width)

rec = create_rectangle()
print(rec)
print("Rectangle Area: ", rec.getArea())

def create_circle():
    color = input("Enter color: ")
    is_filled = input("Is filled?: ").lower() == 'true'
    x_center = float(input("Enter x coordinate of the center: "))
    y_center = float(input("Enter y coordinate of the center: "))
    radius = float(input("Enter radius of the circle: "))
    return Circle(color, is_filled, x_center, y_center, radius)

cir = create_circle()
print(cir)
print("Circle Area: ", cir.getArea())
