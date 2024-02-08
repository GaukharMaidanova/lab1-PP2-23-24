def func(total_heads, total_legs):
    rabbits = (total_legs - 2*total_heads)/2
    chickens = total_heads - rabbits
    print("The total of rabbits: ", int(rabbits))
    print("The total of chickens: ", int(chickens))
x = 35
y = 94
func(x, y)