class MyCalendar:
    def __init__(self):
        self.s = set()

    def book(self, start: int, end: int) -> bool:
        for s, e in self.s:
            if intersect((s, e), (start, end)):
                return False
        self.s.add((start, end))
        return True

def intersect(a: tuple[int, int], b: tuple[int, int]) -> bool:
    (first, second) = (a, b) if a[0] < b[0] else (b, a)
    return second[0] < first[1]


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
