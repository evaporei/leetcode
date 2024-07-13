class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.items = nums
        heapq.heapify(self.items)
        while len(self.items) > self.k:
            heapq.heappop(self.items)

    def add(self, val: int) -> int:
        heapq.heappush(self.items, val)
        if len(self.items) > self.k:
            heapq.heappop(self.items)
        return self.items[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
