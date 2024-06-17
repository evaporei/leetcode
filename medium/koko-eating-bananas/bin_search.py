class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            k = (right + left) // 2
            hours_spent = 0
            for bananas in piles:
                hours_spent += math.ceil(bananas / k)
            if hours_spent <= h:
                right = k - 1
            else:
                left = k + 1

        return left
