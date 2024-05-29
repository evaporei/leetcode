class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0

        def area(i: int, j: int) -> int:
            min_height = min(height[i], height[j])
            return min_height * (j - i)

        left = 0
        right = len(height) - 1

        while left < right:
            m = max(m, area(left, right))
            if height[left] > height[right]:
                right -= 1
            else:
                # it doesn't matter who we shift at this point
                left += 1

        return m
