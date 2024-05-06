class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        freq = [n for n, c in sorted(counts.items(), key=lambda item: item[1], reverse=True)]
        return freq[:k]
