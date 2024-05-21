BUCKETS = 1000

class ListNode:
    key: int
    value: int
    next: "ListNode | None"

    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    entries: list[ListNode]

    def __init__(self):
        self.entries = [ListNode()] * BUCKETS
    
    def get_bucket(self, key: int) -> int:
        return key % BUCKETS

    def put(self, key: int, value: int) -> None: 
        curr = self.entries[self.get_bucket(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next

        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        curr = self.entries[self.get_bucket(key)].next
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        curr = self.entries[self.get_bucket(key)]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
            curr = curr.next
