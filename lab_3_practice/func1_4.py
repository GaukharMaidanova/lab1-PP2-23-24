import math
def filter_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

list_1 = [int(i) for i in input().split()]
list_2=[]
for x in list_1:
    if(filter_prime(x)==True):
        list_2.append(x)
print(list_2)

