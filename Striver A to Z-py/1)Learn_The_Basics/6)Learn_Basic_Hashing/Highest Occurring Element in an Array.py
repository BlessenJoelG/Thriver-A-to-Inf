class Solution:
    def mostFrequentElement(self, nums):
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        maxEle = 0
        maxOcr = 0
        for val,count in freq.items():
            if count>maxOcr:
                maxOcr = count
                maxEle = val
        return maxEle