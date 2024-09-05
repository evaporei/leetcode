class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647

        queue = deque()

        def addRoom(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == INF: 
                queue.append((r, c))
    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = min(distance, grid[r][c])

                addRoom(r - 1, c)
                addRoom(r + 1, c)
                addRoom(r, c - 1)
                addRoom(r, c + 1)
            distance += 1

