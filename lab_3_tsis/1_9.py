def calculate_running_average(list1=[], list2=[]):
    list3 = []
    list4 = [0]
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if(len(list1)>len(list2)):
                while(len(list2)!=len(list1)):
                    list2.extend(list4)
                if(i==j and list2[j]!=0):
                    av = float((list1[i] + list2[j])/2)
                    list3.append(int(av))
                elif(i==j and list2[j]==0):
                    av = float(list1[i])
                    list3.append(av)

            elif(len(list1)<len(list2)):
                while(len(list1)!=len(list2)):
                    list1.extend(list4)
                if(i==j and list1[i]!=0):
                    av = float((list1[i] + list2[j])/2)
                    list3.append(int(av))
                elif(i==j and list1[i]==0):
                    av = float(list2[j])
                    list3.append(av)
            else:
                if(i==j):
                    av = float((list1[i] + list2[j])/2)
                    list3.append(av)
    print(list3)
list_1 = [int(i) for i in input().split()]
list_2 = [int(i) for i in input().split()]
calculate_running_average(list_1, list_2)


