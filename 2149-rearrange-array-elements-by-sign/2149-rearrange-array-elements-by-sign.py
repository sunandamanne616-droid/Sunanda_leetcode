class Solution(object):
    def rearrangeArray(self, arr):
        pos=0
        neg=1
        ans=[0] * len(arr)
        for i in range(0,len(arr)):
            if arr[i]>0:
                ans[pos]=arr[i]
                pos+=2
            else:
                ans[neg]=arr[i]
                neg+=2
        return ans
            