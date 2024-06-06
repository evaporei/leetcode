class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        (first, second) = (event1, event2) if event1[0] < event2[0] else (event2, event1)
        return second[0] <= first[1]
