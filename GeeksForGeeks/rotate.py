# Given an array, rotate the array by one position in clock-wise direction.
 
# Example 1:
# Input:
# N = 5
# A[] = {1, 2, 3, 4, 5}
# Output:
# 5 1 2 3 4
 
# Example 2:
# Input:
# N = 8
# A[] = {9, 8, 7, 6, 4, 2, 1, 3}
# Output:
# 3 9 8 7 6 4 2 1

def rotate_anti_clockwise(arr,n):
    # print(arr[-1:], arr[0::-1], arr[:])
    return arr[1:] + arr[0::-1]

def rotate_clockwise( arr, n):  
    return arr[-1:] + arr[0:-1:]

print(rotate_anti_clockwise([9, 8, 7, 6, 4, 2, 1, 3],8))
print(rotate_anti_clockwise([1 ,2, 3 ,4, 5],5))
print(rotate_anti_clockwise([1 ,2],2))

print(rotate_clockwise([9, 8, 7, 6, 4, 2, 1, 3],8))
print(rotate_clockwise([1 ,2, 3 ,4, 5],5))
print(rotate_clockwise([1 ,2],2))