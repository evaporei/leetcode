class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        # transpose
        for i in range(len(m)):
            for j in range(i, len(m)):
                tmp = m[i][j]
                m[i][j] = m[j][i]
                m[j][i] = tmp

        # reverse
        for row in m:
            row.reverse()
