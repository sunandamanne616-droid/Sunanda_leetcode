class Solution(object):
    def twoSum(self, arr, target):
        seen={}
        for i in range(len(arr)):
            res=target-arr[i]
            if res in seen:
                return seen[res],i
                break
            else:
                seen[arr[i]]=i
