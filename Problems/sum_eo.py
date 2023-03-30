def sum_eo(n,option):
    sum = 0
    if option.casefold() == "e" :
        for i in range(0,n):
            if(i%2 == 0):
              sum += i  
        return sum
    elif option.casefold() == "o":
        for i in range(0,n):
            if(i%2 != 0):
              sum += i 
        return sum
    else:
        return -1
    

print(sum_eo(10, "e"))
print(sum_eo(7,"o"))
print(sum_eo(10,"spam"))