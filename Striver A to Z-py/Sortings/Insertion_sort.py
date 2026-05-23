nums = [13,46,24,52,28,9]
for i in range(len(nums)):
    j = i
    while(j>0):
        if nums[j]<nums[j-1]:
            nums[j],nums[j-1]=nums[j-1],nums[j]
        j -= 1
print(nums)