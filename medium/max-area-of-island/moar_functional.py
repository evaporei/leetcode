class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = -1
            
            return (1 + dfs(i - 1, j) +
                        dfs(i + 1, j) +
                        dfs(i, j - 1) +
                        dfs(i, j + 1))
        
        max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_size = max(max_size, dfs(i, j))
        return max_size

