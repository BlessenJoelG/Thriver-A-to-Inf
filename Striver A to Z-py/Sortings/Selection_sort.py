nums = [13,46,24,52,28,9]
for i in range(0,len(nums)-1):
    mini = i
    for j in range(i,len(nums)):
        if nums[j]<nums[mini]:
            mini = j
    temp = nums[mini]
    nums[mini] = nums[i]
    nums[i] = temp
print(nums)