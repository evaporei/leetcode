BUCKETS = 1000

class MyHashSet:
    entries: list[list[int]]

    def __init__(self):
        self.entries = [[]] * BUCKETS

    def add(self, key: int) -> None:
        hashed = hash(key)
        bucket = hashed % BUCKETS
        if not key in self.entries[bucket]:
            self.entries[bucket].append(key)

    def contains(self, key: int) -> bool:
        hashed = hash(key)
        bucket = hashed % BUCKETS
        return key in self.entries[bucket]

    def remove(self, key: int) -> None:
        hashed = hash(key)
        bucket = hashed % BUCKETS
        if key in self.entries[bucket]:
            self.entries[bucket].remove(key)
