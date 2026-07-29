class Solution(object):
    def subarraySum(self, nums, k):
        prefix = {0: 1}
        suma = 0
        cnt = 0

        for num in nums:
            suma += num

            if suma - k in prefix:
                cnt += prefix[suma - k]

            prefix[suma] = prefix.get(suma, 0) + 1

        return cnt