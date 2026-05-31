nums = [1, 2, 3, 4, 5]
temp = [0]*len(nums)
for i in range(1,len(nums)):
    temp[i-1] = nums[i]
temp[len(nums)-1] = nums[0]
print(temp)