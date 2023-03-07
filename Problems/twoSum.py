#Given an array of integers NUMS and an integer TARGET, return INDICES of the two numbers such that they add up to TARGET.

def twoSum(nums, target):
    output = []
    for i in range(len(nums)-1):
        if((nums[i] + nums[i+1]) == target):
            output.append(i)
            output.append(i+1)
            break
    print(output)


twoSum([1,3,4,5],4)
twoSum([2,7,11,15],9)
twoSum([3,2,4],6)
twoSum([3,3],6)