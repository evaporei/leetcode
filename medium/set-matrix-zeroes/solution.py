class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        rows = []
        cols = []
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for i in rows:
            for j in range(len(m[i])):
                m[i][j] = 0

        for j in cols:
            for i in range(len(m)):
                m[i][j] = 0
