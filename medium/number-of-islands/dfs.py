class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        (rows, cols) = (len(grid), len(grid[0]))

        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if grid[i][j] != '1':
                return
            grid[i][j] = '#'

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
