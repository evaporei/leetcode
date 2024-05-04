class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        left, right = 0, len(m) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # save
                top_left = m[top][left + i]
                
                m[top][left + i] = m[bottom - i][left]

                m[bottom - i][left] = m[bottom][right - i]
                
                m[bottom][right - i] = m[top + i][right]

                m[top + i][right] = top_left

            left += 1
            right -= 1
