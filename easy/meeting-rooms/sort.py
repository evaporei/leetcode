"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        if len(intervals) <= 1:
            return True
        for i in range(len(intervals) - 1):
            a, b = intervals[i], intervals[i+1]
            if intersect(a, b):
                return False
        return True


def intersect(a: Interval, b: Interval) -> bool:
    # or a.end > b.start
    return b.start < a.end
