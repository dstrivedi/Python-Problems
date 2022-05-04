#Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
#Example 1:

#Input: nums = [1,2,3]
#Output: 6
#Example 2:

#Input: nums = [1,2,3,4]
#Output: 24
#Example 3:

#Input: nums = [-1,-2,-3]
#Output: -6

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums);
        product = [];
        nums.sort(reverse=True);
        min1 = nums[n - 1];
        min2 = nums[n -2 ];
        max0 = nums[0];
        max1 = nums[1];
        max2 = nums[2];
        product1 = min1*min2*max0;
        product2 = max0*max1*max2;
        product.insert(0,product1);
        product.insert(1,product2);
        maxProduct = max(product);
        return maxProduct;
