def square(a1, b1):
    for i in range(a1, b1+1):
        yield i*i

a = int(input())
b = int(input())
squares = square(a, b)
while(a<=b):
    print(next(squares))