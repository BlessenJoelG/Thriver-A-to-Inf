class Solution:
    def pattern3(self, n):
        for i in range(1,n+1):
            pat = ""
            for j in range(1,i+1):
                pat = pat + str(j)
            print(pat)