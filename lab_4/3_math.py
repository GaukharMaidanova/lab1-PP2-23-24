import math
x = int(input("Input number of sides: "))
y = int(input("Input the length of a side: "))
P = x*y
A = y/2
S = math.ceil((A*P)/2)
print("The area of the polygon is: ", S)