import math
def isPrime(num):
    if(num<=1):
        return False
    elif(num==2 or num == 3):
        return True
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if(num%i!=0):
                return True
            return False

def filter_prime(list):
    for i in range(0, len(list)-1):
        if(isPrime(list[i])==True):
            print(list[i])

list_1 = [int(i) for i in input().split()]
filter_prime(list_1)