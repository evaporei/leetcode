class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            curr = intervals[i]
            # newInterval comes before i
            if newInterval[1] < curr[0]:
                res.append(newInterval)
                return res + intervals[i:]
            # new interval comes after i
            elif newInterval[0] > curr[1]:
                res.append(curr)
            # they're overlapping, let's merge
            else:
                newInterval = [min(curr[0], newInterval[0]), max(curr[1], newInterval[1])]

        res.append(newInterval)

        return res

