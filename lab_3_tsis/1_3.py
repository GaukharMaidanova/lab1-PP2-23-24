def get_max(num1, num2, num3):
    max = num1
    if(max<num2 and num2>num3):
        max = num2
    elif(max<num2 and num2<num3 or max>num2 and max<num3):
        max = num3
    else:
        max = num1
    return max
a = int(input())
b = int(input())
c = int(input())
print(get_max(a, b, c))

