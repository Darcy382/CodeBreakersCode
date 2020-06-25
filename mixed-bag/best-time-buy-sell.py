class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) <= 1:
            return 0

        buy = float("inf")
        max_prof = 0

        for price in prices:
            current_prof = price - buy
            if current_prof < 0:
                buy = price
            else:
                max_prof = max(current_prof, max_prof)
        return max_prof
