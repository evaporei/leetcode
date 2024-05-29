class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[1])
        original = image[sr][sc]

        if original == color:
            return image

        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if image[i][j] != original:
                return
            image[i][j] = color

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        dfs(sr, sc)
        
        return image
