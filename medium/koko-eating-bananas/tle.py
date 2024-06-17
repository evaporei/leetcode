class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        max_k = max(piles)
        hours_left = h

        while k <= max_k:
            for bananas in piles:
                hours_left -= math.ceil(bananas / k)
                if hours_left < 0:
                    break
            if hours_left == 0:
                return k
            hours_left = h
            k += 1

        return max_k
