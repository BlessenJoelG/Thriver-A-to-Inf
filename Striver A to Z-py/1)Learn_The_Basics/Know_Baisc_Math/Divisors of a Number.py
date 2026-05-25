class Solution:
    def divisors(self, n):
        k,x,num = n,1,[]
        while(n>0):
            if k%x==0:
                num.append(x)
            x += 1
            n -= 1
        return num