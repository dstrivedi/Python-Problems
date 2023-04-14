# Given an array arr[] of integers. Find a peak element i.e. an element that is not smaller than its neighbors and return indices

# Note: For corner elements, we need to consider only one neighbor. 
# Input: array[]= {5, 10, 20, 15}
# Output: 20
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20. return indices

# Input: array[] = {10, 20, 15, 2, 23, 90, 67}
# Output: 20 or 90
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67. return indices

def peakElement(arr:list, n:int) -> list:
    peak = []
    if(n == 1):
        return [0]
    if(arr[0] >= arr[1]):
        peak.append(0)
    for i in range(len(arr)):
        if(i != len(arr)-1 and (arr[i] >= (arr[i-1])) and (arr[i] >= arr[i+1])):
            # peak.append(arr[i])
            peak.append(i)
    if (arr[n - 1] >= arr[n - 2]):
        peak.append(n-1)
    return peak

print(peakElement([5, 10, 20, 15],4))
print(peakElement([10, 20, 15, 2, 23, 90, 67, 100],8))
print(peakElement([1,2,3],3))
    