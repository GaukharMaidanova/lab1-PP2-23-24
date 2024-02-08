def find_common_elements(list1, list2):
    list3 = []
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if(list1[i]==list2[j]):
                list3.append(list2[j])
            else:
                continue
    print(list3)
lis_1 = [int(i) for i in input().split()]
lis_2 = [int(i) for i in input().split()]
find_common_elements(lis_1, lis_2)