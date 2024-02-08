import math
def volumefunc(radius):
    volume = (4/3) * math.pi * pow(radius, 3)
    print(volume)
radius1 = int(input())
volumefunc(radius1)