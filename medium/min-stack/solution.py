class ListNode:
    val: int
    next: "ListNode | None"
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class MinStack:
    head: ListNode | None
    min_stack: ListNode | None

    def __init__(self):
        self.head = None
        self.min_stack = None

    def push(self, val: int) -> None:
        if self.head:
            min_val = min(val, self.min_stack.val)
            self.head = ListNode(val, self.head)
            self.min_stack = ListNode(min_val, self.min_stack)
        else:
            self.head = ListNode(val)
            self.min_stack = ListNode(val)

    def pop(self) -> None:
        if self.head:
            self.head = self.head.next
            self.min_stack = self.min_stack.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.min_stack.val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
