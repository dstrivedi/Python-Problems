def fibonacci(n:int) -> list:
    """Returnn the `n`th fibonacci number, for positive `n`."""
    result = []
    sum = 0
    for i in range(n):
        if(i == 0): 
            result.append(0)
        elif(i == 1): 
            result.append(1)
        else:
            sum = result[i-1] + result[i-2]
            result.append(sum)
    return result
         

print(fibonacci(7))
print(fibonacci(5))