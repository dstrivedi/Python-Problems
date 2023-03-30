def factorial_recurssion(n) -> int:
    """ Return factorial of a number"""
    return 1 if(n==1 or n==0) else n*factorial_recurssion(n-1)
    #return 

def factorial(n:int) -> int:
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

for i in range(36):
    print(i, factorial(i))

print("-"*10, " using recursion " , "-"*10)
print(factorial_recurssion(6))
print(factorial_recurssion(4))