class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        fst = 0
        sec = 1
        thr = 0

        for _ in range(2, n + 1):
            thr = fst + sec
            fst = sec
            sec = thr

        return thr
