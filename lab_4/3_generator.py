def func(num):
    gen = (_iter for _iter in range(0, num+1) if _iter%3==0 and _iter%4==0)
    i=0
    while(i<=num):
        print(next(gen))
        i+=1

n = int(input("enter N: "))
func(n)