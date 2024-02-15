import math
n = int(input("Enter N: "))
gen = (int(math.pow(_n, 2)) for _n in range(0, n+1))
i = 0
while(i<=n):
    print(next(gen))
    i+=1
