def isPalindrome(x):
  result = 0
  original = x
  while(x > 0):
    n = x % 10
    result = result * 10 + n
    x = x // 10
  # print(result)
  return result == original

def usingSlicing(x):
  #using slicing
  if(str(x) == str(x)[::-1]):
    return "num is palindrome"
  else:
    return "num is not palindrome"
  
print(isPalindrome(123))
print(isPalindrome(121))
print(isPalindrome(16461))
print(isPalindrome(2345))
