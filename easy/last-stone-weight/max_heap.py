class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # turn into a max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        weight = 0
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0

        
