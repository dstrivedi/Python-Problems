def fibonacci(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer!"
    if (n in [0, 1]):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#print 4th number
print(fibonacci(4))

n = 4
#print series
for i in range(n):
  print(fibonacci(i))
