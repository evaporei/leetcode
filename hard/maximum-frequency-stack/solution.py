class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.max_count = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        self.count[val] += 1
        new_count = self.count[val]
        if new_count > self.max_count:
            self.max_count = new_count
            self.stacks[new_count] = []
        self.stacks[new_count].append(val)

    def pop(self) -> int:
        val = self.stacks[self.max_count].pop()
        self.count[val] -= 1
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
