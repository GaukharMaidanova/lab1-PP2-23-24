def isEven(num):
    if(num%2==0):
        return True
    return False
n = int(input())
if(isEven(n)==True):
    print("True")
else:
    print("False")