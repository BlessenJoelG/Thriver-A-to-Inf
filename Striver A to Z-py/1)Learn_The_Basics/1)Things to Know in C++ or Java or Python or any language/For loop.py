class Solution:
    def forLoop(self, low : int, high : int) -> int:
        c = 0
        for i in range(low,high+1):
            c += i
        return c