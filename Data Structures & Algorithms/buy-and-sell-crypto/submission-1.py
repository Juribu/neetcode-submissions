class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # slide right until the difference value get bigger
        # slide left
        l = 0
        r = 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        return maxP

        