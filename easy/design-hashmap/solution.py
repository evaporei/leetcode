BUCKETS = 1000

class MyHashMap:
    entries: list[list[int]]

    def __init__(self):
        self.entries = [[]] * BUCKETS

    def put(self, key: int, value: int) -> None:
        hashed = hash(key)
        bucket = hashed % BUCKETS
        
        for i, (k, v) in enumerate(self.entries[bucket]):
            if k == key:
                self.entries[bucket][i] = (key, value)
                return
        self.entries[bucket].append((key, value))

    def get(self, key: int) -> int:
        hashed = hash(key)
        bucket = hashed % BUCKETS
        for k, v in self.entries[bucket]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        hashed = hash(key)
        bucket = hashed % BUCKETS
        index = -1
        for i, pair in enumerate(self.entries[bucket]):
            k, v = pair
            if k == key:
                index = i
                break
        if index != -1:
            del self.entries[bucket][index]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
