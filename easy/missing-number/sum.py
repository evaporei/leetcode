class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums) + 1):
            s += i
        s2 = 0
        for n in nums:
            s2 += n
        return s - s2
