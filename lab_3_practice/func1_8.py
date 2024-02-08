def order(numbers):
    for i in range(0,len(numbers)):
        if numbers[i] == 0:
            for j in range(i+1, len(numbers)):
                if numbers[j] == 0:
                    for k in range(i+2, len(numbers)):
                        if numbers[k] == 7:
                            return True
                    return False
                
list_1 = [int(i) for i in input().split()]
if order(list_1) == True:
    print("True")
elif order(list_1) == False:
    print("False")