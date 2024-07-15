class LRUCache:

    def __init__(self, capacity: int):
        self.items = {}
        self.cap = capacity
        self.lru = []

    def get(self, key: int) -> int:
        if key in self.items:
            if key not in self.lru:
                self.lru.append(key)
            else:
                self.lru.remove(key)
                self.lru.append(key)
            return self.items[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.items[key] = value
        if key in self.lru:
            self.lru.remove(key)
        self.lru.append(key)
        if len(self.lru) > self.cap:
            del_key = self.lru.pop(0)
            del self.items[del_key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
