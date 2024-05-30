class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [height[0]]
        for i in range(1, len(height)):
            max_left.append(max(max_left[i-1], height[i]))

        max_right = [0] * len(height)
        max_right[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        res = 0
        for i in range(len(height)):
            res += min(max_left[i], max_right[i]) - height[i]

        return res
