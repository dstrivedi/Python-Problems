#Avoid Spaces in string length
def countChar(str):
    cnt = 0
    for i in range(len(str)):
        if(str[i]!=" "):
            cnt += 1
    return cnt

str = "geeksforgeeks 33 best"
cnt = sum(not chr.isspace() for chr in str)
print(cnt)

print(countChar("drashti sagar"))
print(countChar("geeksforgeeks 33 best"))