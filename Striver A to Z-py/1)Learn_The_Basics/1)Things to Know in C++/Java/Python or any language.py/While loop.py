class Solution:
    def whileLoop(self, d : int) -> int:
        num,n,c = 1,0,0
        while(n!=50):
            if num%10 == d:
                c += num
                n += 1
            num += 1
        return c