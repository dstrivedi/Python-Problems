def removeChar(str,ind):
    # li = list(str)
    # li.remove(str[ind])
    # return "".join(li)
    return str[:ind] + str[ind+1:]

print(removeChar("drashti",2))
print(removeChar("GeeksForGeeks",3))