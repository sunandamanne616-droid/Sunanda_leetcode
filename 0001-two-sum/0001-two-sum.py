class Solution(object):
    def twoSum(self, arr, target):
        seen={}
        for i in range(0,len(arr)):
            rem=target-arr[i]
            if rem in seen:
                return i,seen[rem]
                break
            seen[arr[i]]=i
        

