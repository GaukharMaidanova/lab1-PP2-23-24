def unique(numbs):
    empty_list = []
    for item in numbs: 
        if item not in empty_list: 
            empty_list.append(item)
    print(empty_list)

list_1 = [int(i) for i in input().split()]
unique(list_1)


