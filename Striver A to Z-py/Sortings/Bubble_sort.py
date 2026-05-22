nums = [13,46,24,52,28,9]
n = len(nums)

#my-logical-thinking-version
for _ in range(n):
    swaps = 0
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            swaps += 1
    if swaps == 0:
        break
    n -= 1
print(nums)

#striver-version
for i in range(n-1,-1,-1):
    swaps = 0
    for j in range(i):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            swaps += 1
    if swaps == 0:
        break
print(nums)