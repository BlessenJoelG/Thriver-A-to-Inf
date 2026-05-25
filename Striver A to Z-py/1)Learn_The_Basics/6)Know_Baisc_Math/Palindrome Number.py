class Solution:
    def isPalindrome(self, n):
        x,num = n,0
        while(n>0):
            s = n%10
            num = num*10+s
            n = n//10
        return x == num