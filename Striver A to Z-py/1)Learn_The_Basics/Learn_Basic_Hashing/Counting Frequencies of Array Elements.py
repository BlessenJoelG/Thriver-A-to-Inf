class Solution:
    def countFrequencies(self, nums):
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        ele = []
        for i in freq.items():
            ele.append(list(i))
        return(ele)