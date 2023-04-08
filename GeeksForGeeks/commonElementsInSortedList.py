def commonElements(a,b,c,n1,n2,n3):
    return sorted(list(set(c).intersection(b).intersection(a)))

print(commonElements([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120], 6, 5, 8))
print(commonElements([3,3,3],[3,3,3],[3,3,3],3,3,3))