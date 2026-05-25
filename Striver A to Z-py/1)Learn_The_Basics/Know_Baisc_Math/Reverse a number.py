class Solution:
    def reverseNumber(self, n):
        num = 0
        while(n>0):
            s = n%10
            num = num*10+s
            n = n//10
        return num