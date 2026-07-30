class Solution(object):
    def getRow(self, n):
        res = 1
        ans=[]

        for c in range(n+1):
            ans.append(res)
            res = res * (n - c) // (c + 1)

        return ans