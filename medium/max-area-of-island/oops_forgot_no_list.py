class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, size: int):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return size
            if grid[i][j] != 1:
                return size
            grid[i][j] = -1
            
            size += 1
            
            size = dfs(i - 1, j, size)
            size = dfs(i + 1, j, size)
            size = dfs(i, j - 1, size)
            return dfs(i, j + 1, size)
        
        max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_size = max(max_size, dfs(i, j, 0))
        return max_size

