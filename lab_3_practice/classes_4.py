import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, x_1, y_1):
        n = int(input("Parameter to move by x axis: "))
        m = int(input("Parameter to move by y axis: "))
        x_1 = self.x + n
        y_1 = self.y + m
        self.x_1 = x_1
        self.y_1 = y_1
        print(self.x_1, self.y_1)

    def distance(self):
        dist = math.sqrt((self.x_1 - self.x)*(self.x_1 - self.x) + (self.y_1 - self.y)*(self.y_1 - self.y))
        print(dist)

coor_x = int(input())
coor_y = int(input())
ppt = Point(coor_x, coor_y)
ppt.show()
ppt.move()
ppt.distance()