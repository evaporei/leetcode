class MyCalendar:
    def __init__(self):
        self.calendar = []
    
    def find_position(self, start: int, end: int) -> int:
        if not self.calendar:
            return 0
        low, high = 0, len(self.calendar) - 1
        while low <= high:
            mid = (low + high) // 2
            [s, e] = self.calendar[mid]
            if e <= start:
                low = mid + 1
            elif s >= end:
                high = mid - 1
            else:
                return -1
        return low

    def book(self, start: int, end: int) -> bool:
        i = self.find_position(start, end)
        if i != -1:
            self.calendar.insert(i, (start, end))
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
