class ListNode:
    val: int
    next: "ListNode | None"
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class Stack:
    head: ListNode
    length: int
    def __init__(self):
        self.head = ListNode()
        self.length = 0
    
    def push(self, val: int):
        self.head = ListNode(val, self.head)
        self.length += 1
    
    def pop(self) -> int:
        val = self.head.val
        if val != -1:
            self.head = self.head.next
            self.length -= 1
        return val
    
    def peek(self) -> int:
        return self.head.val

    def size(self) -> int:
        return self.length
    
    def empty(self) -> bool:
        return self.size() == 0

class MyQueue:
    push_stack: Stack
    pop_stack: Stack

    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def push(self, x: int) -> None:
        self.push_stack.push(x)

    def populate_pop_stack(self):
        if self.pop_stack.empty():
            while not self.push_stack.empty():
                el = self.push_stack.pop()
                self.pop_stack.push(el)

    def pop(self) -> int:
        self.populate_pop_stack()
        return self.pop_stack.pop()

    def peek(self) -> int:
        self.populate_pop_stack()
        return self.pop_stack.peek()

    def empty(self) -> bool:
        return self.push_stack.empty() and self.pop_stack.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
