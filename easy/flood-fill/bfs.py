class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[1])
        original = image[sr][sc]

        if original == color:
            return image

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()

        def bfs(i: int, j: int):
            queue = collections.deque()
            queue.append((i, j))
            visited.add((i, j))
            image[i][j] = color

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = (r + dr, c + dc)
                    if (0 <= row < rows and
                        0 <= col < cols and
                        image[row][col] == original and
                        (row, col) not in visited):
                        visited.add((row, col))
                        queue.append((row, col))
                        image[row][col] = color
        
        bfs(sr, sc)
        
        return image
