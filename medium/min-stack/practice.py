class Node:
    val: int
    min_so_far: int
    next: "Node | None"
    
    def __init__(self, val: int, min_so_far: int, nxt = None):
        self.val = val
        self.min_so_far = min_so_far
        self.next = nxt

class MinStack:
    stack: Node | None

    def __init__(self):
        self.stack = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack = Node(val, val)
        else:
            new_node = Node(val, min(self.stack.min_so_far, val), self.stack)
            self.stack = new_node

    def pop(self) -> None:
        self.stack = self.stack.next

    def top(self) -> int:
        return self.stack.val

    def getMin(self) -> int:
        return self.stack.min_so_far
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
