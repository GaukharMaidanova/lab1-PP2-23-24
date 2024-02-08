def palindrome(string_1):
    string_2 = string_1[::-1]
    if string_1 == string_2:
        return True
    return False
string = input()
if palindrome(string) == True:
    print("Yes, palindrome")
else:
    print("No")