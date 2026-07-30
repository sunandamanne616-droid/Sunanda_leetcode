class Solution(object):
    def generate(self, n):
        ans=[]
        def ncr(n,r):
            res=1
            for i in range(r):
                res=res*(n-i)
                res=res//(i+1)
            return res
        for row in range(n):
            temp=[]
            for col in range(row+1):
                temp.append(ncr(row,col))
            ans.append(temp)
        return ans
        