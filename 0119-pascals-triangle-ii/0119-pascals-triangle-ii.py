class Solution(object):
    def getRow(self, n):
        ans = []

        def ncr(n, r):
            res = 1
            for i in range(r):
                res = res * (n - i)
                res = res // (i + 1)
            return res

        for c in range(n + 1):
            ans.append(ncr(n, c))

        return ans