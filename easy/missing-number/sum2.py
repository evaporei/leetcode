class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
        s2 = 0
        for i in range(len(nums)):
            s += i
            s2 += nums[i]
        return s - s2
