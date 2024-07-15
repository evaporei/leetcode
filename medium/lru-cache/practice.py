class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.next = self.prev = None

# d o u b l y
class LinkedList:
    def __init__(self):
        # least and most recently used lists
        self.least, self.most = Node(0, 0), Node(0, 0)
        # least ---next---> most
        # least <--prev---- most
        self.least.next, self.most.prev = self.most, self.least
    
    # at most used side
    def insert(self, node: Node):
        # a --next--> most
        # to:
        # a --next--> node --next--> most
        # same thing for prev pointers
        prev, nxt = self.most.prev, self.most
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    # from least used side
    def remove(self, node: Node):
        # a --next--> node --next--> b
        # to:
        # a --next--> b
        # same thing for prev pointers
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # key to node (in either of the lists)
        self.cache = {}
        self.freq_list = LinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.freq_list.remove(node)
            self.freq_list.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.freq_list.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.freq_list.insert(node)
        
        if len(self.cache) > self.cap:
            lru = self.freq_list.least.next
            self.freq_list.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
