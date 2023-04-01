def sum_numbers(*args:float) ->float:
    """Return sum of numbers"""
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))

