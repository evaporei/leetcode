class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        start = word[0]

        def dfs(i: int, j: int, ch: int) -> bool:
            if ch == len(word):
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False
            if board[i][j] != word[ch]:
                return False
            tmp = board[i][j]
            board[i][j] = '#'

            next_ch = ch + 1

            if (dfs(i - 1, j, next_ch) or
                    dfs(i + 1, j, next_ch) or
                    dfs(i, j - 1, next_ch) or
                    dfs(i, j + 1, next_ch)):
                return True
            
            board[i][j] = tmp
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == start and dfs(i, j, 0):
                    return True
