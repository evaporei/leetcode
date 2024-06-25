class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        weight = 0
        while stones:
            if len(stones) == 1:
                return stones[0]
            y = stones.pop()
            x = stones.pop()
            if x != y:
                stones.append(abs(y - x))
                stones.sort()

        return weight

        
