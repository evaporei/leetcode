BUCKETS = 1000

class ListNode:
    key: int
    next: "ListNode | None"

    def __init__(self, key=-1):
        self.key = key
        self.next = None

class MyHashSet:
    entries: list[ListNode]

    def __init__(self):
        self.entries = [ListNode()] * BUCKETS
    
    def get_bucket(self, key: int) -> int:
        return key % BUCKETS

    def add(self, key: int) -> None:
        curr = self.entries[self.get_bucket(key)]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next

        curr.next = ListNode(key)

    def contains(self, key: int) -> bool:
        curr = self.entries[self.get_bucket(key)].next
        while curr:
            if curr.key == key:
                return True
            curr = curr.next

        return False

    def remove(self, key: int) -> None:
        curr = self.entries[self.get_bucket(key)]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
