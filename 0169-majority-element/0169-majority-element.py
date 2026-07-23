class Solution(object):
    def majorityElement(self, arr):
        maj=len(arr)//2
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1
        for k,v in freq.items():
            if v>maj:
                return k
        