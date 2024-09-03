class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def dfs(i: int, j: int):
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[i]) - 1:
                return
            if grid[i][j] != '1' or (i, j) in visited:
                return
            visited.add((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands += 1
                    dfs(i, j)
        
        return islands
            
