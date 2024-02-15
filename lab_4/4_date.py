import datetime
def date_dif(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d-%H:%M:%S")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d-%H:%M:%S")
    return abs((d2-d1).seconds)

d1 = str(input("Enter 1st date: "))
d2 = str(input("Enter 2nd date: "))
print(date_dif(d1, d2))