class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return bs(matrix, target, 0, len(matrix) * len(matrix[0]) - 1)

def bs(m: List[List[int]], target: int, low: int, high: int) -> bool:
    if low <= high:
        mid = (high - low) // 2 + low
        i = mid // len(m[0])
        j = mid % len(m[0])
        if target > m[i][j]:
            return bs(m, target, mid + 1, high)
        elif target < m[i][j]:
            return bs(m, target, low, mid - 1)
        else:
            return True
    else:
        return False
