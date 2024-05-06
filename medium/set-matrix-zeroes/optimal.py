class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        ROWS, COLS = len(m), len(m[0])
        row_zero = False
        for r in range(ROWS):
            for c in range(COLS):
                if m[r][c] == 0:
                    m[0][c] = 0
                    if r > 0:
                        m[r][0] = 0
                    else:
                        row_zero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if m[r][0] == 0 or m[0][c] == 0:
                    m[r][c] = 0

        if m[0][0] == 0:
            for r in range(ROWS):
                m[r][0] = 0

        if row_zero:
            for c in range(COLS):
                m[0][c] = 0
