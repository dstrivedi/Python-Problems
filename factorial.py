def factorial(n):
    return 1 if(n==1 or n==0) else n*factorial(n-1)
    #return 

print(factorial(6))
print(factorial(4))