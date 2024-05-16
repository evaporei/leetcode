class Solution:
    def generate(self, n: int) -> List[List[int]]:
        pt = []
        for row in range(n):
            new_row = [1] * (row + 1)
            for i in range(1, row):
                new_row[i] = pt[row - 1][i - 1] + pt[row - 1][i]
            pt.append(new_row)
        return pt

