class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        val = ""
        low = 0
        high = len(self.m[key]) - 1

        while low <= high:
            mid = (high + low) // 2
            ts = self.m[key][mid][0]
            if ts == timestamp:
                return self.m[key][mid][1]
            elif ts < timestamp:
                val = self.m[key][mid][1]
                low = mid + 1
            else:
                high = mid - 1 
        
        return val
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
