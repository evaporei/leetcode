class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        finals = prices.copy()
        for i, price in enumerate(prices):
            j = i + 1
            while j < len(prices):
                if prices[j] <= price:
                    finals[i] -= prices[j]
                    break
                j += 1
        return finals
