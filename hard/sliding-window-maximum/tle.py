class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, k - 1
        res = []

        while right < len(nums):
            window = nums[left:right+1]
            res.append(max(window))
            left += 1
            right += 1
        
        return res

