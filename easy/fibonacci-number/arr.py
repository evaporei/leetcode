class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        res = [0] * (n + 1)
        res[1] = 1
        for i in range(2, n+1):
            res[i] = res[i - 2] + res[i - 1]
        return res[n]
