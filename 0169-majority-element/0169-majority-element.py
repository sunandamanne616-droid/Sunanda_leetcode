class Solution:
    def majorityElement(self, nums):
        maj=len(nums)//2
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for k,v in freq.items():
            if v>maj:
                return k

        