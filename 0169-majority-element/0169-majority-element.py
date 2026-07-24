class Solution:
    def majorityElement(self, nums):
        can = None
        count = 0

        for i in nums:
            if count == 0:
                can = i

            if i == can:
                count += 1
            else:
                count -= 1

        return can