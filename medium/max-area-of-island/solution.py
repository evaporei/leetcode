class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int):
            nonlocal size
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] != 1:
                return
            grid[i][j] = -1

            size += 1
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        sizes = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size = 0
                    dfs(i, j)
                    sizes.append(size)
        if not sizes:
            return 0
        return max(sizes)

