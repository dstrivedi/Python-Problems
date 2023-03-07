def reverseStr(str):
    assert str != " " , "String must not be empty"
    if len(str) <= 1:
        return str
    return str[len(str)-1] + reverseStr(str[0:len(str)-1])

print(reverseStr("python"))