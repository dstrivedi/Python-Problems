def fact(n):
    assert n >= 0 and int(n), 'The number must be positive integer!'
    if n in [0, 1]:
        return 1
    else:
        return n * fact(n - 1)


print(fact(4))
print(fact(6))
print(fact(10))
print(fact(-1))
