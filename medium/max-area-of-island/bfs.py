class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def bfs(start: tuple[int, int]) -> int:
            queue = deque([start])
            visited.add(start)
            area = 1

            while queue:
                i, j = queue.popleft()
                for direction in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    r, c = direction
                    if (0 <= r < rows and
                        0 <= c < cols and
                        direction not in visited and
                        grid[r][c] == 1):
                        area += 1
                        queue.append(direction)
                        visited.add(direction)
            
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(maxArea, bfs((i, j)))

        return maxArea
