nums = [8, 8, 7, 6, 5]
nums.sort()
largest = nums[len(nums)-1]
seclargest = -1
for i in range(len(nums)-1,-1,-1):
    if nums[i]<largest:
        seclargest = nums[i]
        break
print(seclargest)
#recursive approach ~ O(2^n) 
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)

#iterative approach ~ O(n)       
class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        for i in range(n):
            a,b = b,a+b
        return a
