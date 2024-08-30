def palindrome(s: str, i: int, j: int) -> bool:
    left, right = i, j+1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i: int, curr: List[int]):
            if i >= len(s):
                res.append(curr)
                return
            for j in range(i, len(s)):
                if palindrome(s, i, j):
                    dfs(j + 1, curr + [s[i:j+1]])
        dfs(0, [])
        return res
