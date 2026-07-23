class Solution(object):
    def maxSubArray(self, nums):
        cur_sum=0
        res = nums[0]
        for n in nums:
            cur_sum+=n
            res=max(res,cur_sum)
            if cur_sum<0:
                cur_sum=0
        return res
        