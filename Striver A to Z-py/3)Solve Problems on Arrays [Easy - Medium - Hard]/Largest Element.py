class Solution:
    def largestElement(self, nums):
        maxi = 0
        for i in range(len(nums)):
            if maxi<nums[i]:
                maxi = nums[i]
        return maxi