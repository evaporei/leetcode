from heapq import heappush, nlargest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heappush(h, n)
        return nlargest(k, h)[-1]
