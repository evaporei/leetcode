class Solution:
    def climbStairs(self, n: int) -> int:
        return aux({}, n)

def aux(memo: dict[int, int], n: int) -> int:
    if n <= 1:
        return 1
    if n not in memo:
        memo[n] = aux(memo, n - 1) + aux(memo, n - 2)
    return memo[n]
