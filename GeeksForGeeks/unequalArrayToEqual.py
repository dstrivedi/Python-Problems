# You are given two arrays A and B each of length N. You can perform the following operation on array A zero or more times.

# Select any two indices i and j, 1 <= i , j <= N and i != j
# Set A[i] = A[i] + 2 and A[j] = A[j]-2
# Find the minimum number of operations required to make A and B equal.

# Note :

# Two arrays are said to be equal if the frequency of each element is equal in both of them.
# Arrays may contain duplicate elements.

def unequalArrays(nums: list, target: list, N: int):
    moves = 0
    nums.sort(key = lambda x: (x % 2, x))
    target.sort(key = lambda x: (x % 2, x))
    # print(nums)
    for i in range(len(nums)):
        cnt = (nums[i] - target[i]) // 2
        # print(cnt)z
        if(cnt > 0) :
            moves += cnt
    return moves


print(unequalArrays([8,12,6], [2,14,10], 3))
print(unequalArrays([1,2,5], [4,1,3],3))
print(unequalArrays([2,5,6],[1,2,10],3))
print(unequalArrays([3,3],[9,8],2))
