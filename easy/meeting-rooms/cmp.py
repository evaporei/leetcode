"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        for i in range(len(intervals) - 1):
            a, b = intervals[i], intervals[i+1]
            if intersect(a, b):
                return False
        return True


def intersect(a: Interval, b: Interval) -> bool:
    a, b = (a, b) if a.start < b.start else (b, a)
    return b.start < a.end
