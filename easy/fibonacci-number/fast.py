cache = {
    0: 0,
    1: 1
}

class Solution:
    def fib(self, n: int) -> int:
        if n in cache:
            return cache[n]
        cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return cache[n]
