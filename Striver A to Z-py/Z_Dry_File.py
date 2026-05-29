nums = [8, 8, 7, 6, 5]
nums.sort()
largest = nums[len(nums)-1]
seclargest = -1
for i in range(len(nums)-1,-1,-1):
    if nums[i]<largest:
        seclargest = nums[i]
        break
print(seclargest)
