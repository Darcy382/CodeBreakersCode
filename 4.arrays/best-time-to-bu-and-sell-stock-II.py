# First attempt O(N) time and O(1) space
def maxProfit(self, prices) -> int:
    end = len(prices)
    profit = 0
    i = 0
    while i < end:
        if i + 1 < end and prices[i + 1] > prices[i]:
            buy_in = prices[i]
            while i + 1 < end and prices[i + 1] > prices[i]:
                i += 1
            profit += prices[i] - buy_in
        i += 1
    return profit

# Second attempt, try to simplify, without using the while loops