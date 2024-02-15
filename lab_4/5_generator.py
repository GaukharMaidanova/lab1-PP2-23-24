def func(num):
    for i in range(num, -1, -1):
        yield i

n = int(input())
gen = func(n)
i = 0
while(i<=n):
    print(next(gen))
    i+=1