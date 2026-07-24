class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        profit = 0

        for p in prices:
            min_price=min(p,min_price)
            profit=max(profit,p-min_price)
        return profit