class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            left, right = height[l], height[r]
            area = min(left, right) * (r - l)
            max_area = max(max_area, area)
            if left < right:
                l += 1
            else:
                r -= 1

        return max_area
