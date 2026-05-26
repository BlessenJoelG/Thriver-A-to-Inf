class Solution:
    def pattern6(self, n):
        for i in range(n,-1,-1):
            pat = ""
            for j in range(1,i+1):
                pat = pat+str(j)
            print(pat)