class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        w, h = len(matrix[0]), len(matrix)
        res = [[0 for _ in range(h)] for _ in range(w)]
        for i in range(h):
            for j in range(w):
                res[j][i] = matrix[i][j]
        return res
