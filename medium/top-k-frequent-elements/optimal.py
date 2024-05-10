class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in counts.items():
            buckets[c].append(n)
        k_freq = []
        for bucket in reversed(buckets): # buckets[::-1]
            while bucket:
                k_freq.append(bucket.pop())
                if len(k_freq) == k:
                    return k_freq
