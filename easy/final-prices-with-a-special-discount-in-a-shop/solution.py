class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        finals = prices.copy()
        for i, price in enumerate(prices):
            for discount in prices[i+1:]:
                if discount <= price:
                    finals[i] -= discount
                    break
        return finals
