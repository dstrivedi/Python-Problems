def recursiveRange(num):
    if num == 0:
        return num
    return num + recursiveRange(num - 1)


print(recursiveRange(6))
