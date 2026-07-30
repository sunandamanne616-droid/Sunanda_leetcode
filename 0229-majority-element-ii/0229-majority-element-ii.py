class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        limit=n/3
        freq={}
        ans=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for k,v in freq.items():
            if v>limit:
                ans.append(k)
        return ans
        