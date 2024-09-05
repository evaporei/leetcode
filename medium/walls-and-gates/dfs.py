class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])

        def dfs(i: int, j: int, distance: int):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if rooms[i][j] < distance:
                return
            rooms[i][j] = distance

            dfs(i - 1, j, distance + 1)
            dfs(i + 1, j, distance + 1)
            dfs(i, j - 1, distance + 1)
            dfs(i, j + 1, distance + 1)
            
    
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)

