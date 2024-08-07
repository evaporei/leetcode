class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.m[key]) - 1
        res = ''
        
        while left <= right:
            mid = (left + right) // 2
            ts, val = self.m[key][mid]
            if ts > timestamp:
                right = mid - 1
            elif ts < timestamp:
                res = val
                left = mid + 1
            else:
                return val

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
