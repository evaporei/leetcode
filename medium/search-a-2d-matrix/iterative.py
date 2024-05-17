class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0]) - 1

        while low <= high:
            mid = (high - low) // 2 + low
            i = mid // len(matrix[0])
            j = mid % len(matrix[0])
            if target > matrix[i][j]:
                low = mid + 1
            elif target < matrix[i][j]:
                high = mid - 1
            else:
                return True
        
        return False
