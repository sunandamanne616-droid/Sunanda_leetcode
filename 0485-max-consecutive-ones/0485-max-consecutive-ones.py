class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi=0
        cnt=0
        for n in nums:
            if n ==1:
                cnt+=1
                maxi=max(maxi,cnt)
            else:
                cnt=0
        return maxi
        