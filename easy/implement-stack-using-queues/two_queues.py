class MyStack:
    def __init__(self):
        self.front = deque()
        self.back = deque()

    def push(self, x: int) -> None:
        self.front.append(x)

    def pop(self) -> int:
        while len(self.front) > 1:
            self.back.append(self.front.popleft())
        res = self.front.popleft()
        self.front, self.back = self.back, self.front
        return res

    def top(self) -> int:
        while len(self.front) > 1:
            self.back.append(self.front.popleft())
        res = self.front[0]
        self.back.append(self.front.popleft())
        self.front, self.back = self.back, self.front
        return res
        
    def empty(self) -> bool:
        return not self.front


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
