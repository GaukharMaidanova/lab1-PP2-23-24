def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

list_1 = [int(i) for i in input().split()]
if has_33(list_1) == True:
    print("True")
elif has_33(list_1) == False:
    print("False")