# newList = [ expression(element) for element in oldList if condition ] 

print("Even list : ",[char for char in [1,2,3,4,5,6] if char % 2 == 0])

matrix = [[j for j in range(3)] for i in range(5)]
print("Matrix : ", matrix)

print([char for char in "Geeks for Geeks"])

print([i*10 for i in range(1,11)])