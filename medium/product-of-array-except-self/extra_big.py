class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * (len(nums) + 2)
        # 1 to n
        for i in range(len(nums)):
            left[i] = left[i - 1] * nums[i]
        
        right = [1] * (len(nums) + 2)
        right[-1] = nums[-1]
        # n-1 to 0
        for i in reversed(range(len(nums))):
            right[i] = right[i + 1] * nums[i]

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = left[i - 1] * right[i + 1]
        return res
