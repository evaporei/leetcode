class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = deque()

        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        if fresh == 0:
            return 0

        minutes = 0
        newRotten = False

        while queue:
            for _ in range(len(queue)):
                # rotten
                i, j = queue.popleft()

                # adjacent
                for direction in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    r, c = direction
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        continue
                    if grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] = 2
                        queue.append((r, c))
                        newRotten = True
            if newRotten:
                minutes += 1
                newRotten = False

        return minutes if fresh == 0 else -1
