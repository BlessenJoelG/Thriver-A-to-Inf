class Solution:
    def isArmstrong(self, n):
        x,num = n,0
        while(n>0):
            s = n%10
            num = num+s**len(str(x))
            n = n//10
        return x == num
        