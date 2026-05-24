class Solution:
    def reverseArray(self,n,x):
        x[:] = x[::-1]
        return x