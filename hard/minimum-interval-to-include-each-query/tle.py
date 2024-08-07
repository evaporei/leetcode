class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for query in queries:
            smallest = float('inf')
            for left, right in intervals:
                if query in range(left, right + 1):
                    smallest = min(smallest, right - left + 1)
            res.append(smallest if smallest != float('inf') else -1)
        
        return res
