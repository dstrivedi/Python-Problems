def isPalindrome(x):
    #using slicing
    if(str(x) == str(x)[::-1]):
      print("num is palindrome")
    else:
      print("num is not palindrome")


isPalindrome(16461)
isPalindrome(2345)