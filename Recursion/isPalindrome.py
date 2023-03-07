def isPalindrome(num, temp):
    if num == 0:
        return temp;

    temp = (temp*10)+(num%10)
    return isPalindrome(num//10,temp)
    # if(len(str(num)) <= 1):
    #     return True
    # if(str(num)[0] != str(num)[-1]):
    #     return False
    # else:
    #     return isPalindrome(str(num)[1:-1])

num = 3456
temp = isPalindrome(num,0)
if(num == temp):
    print("True")
else:
    print("False")
num1 = 1221
temp1 = isPalindrome(num1,0)
if(num1 == temp1):
    print("True")
else:
    print("False")
