class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_n: int, close_n: int, s: list[str]):
            if open_n == close_n == n:
                res.append(''.join(s))
                return
            
            if open_n < n:
                backtrack(open_n + 1, close_n, s + ['('])
            
            if close_n < open_n:
                backtrack(open_n, close_n + 1, s + [')'])
                
        backtrack(0, 0, [])
        return res

