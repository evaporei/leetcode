from itertools import islice

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        curr = 1
        longest = curr
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue

            if nums[i] + 1 == nums[i + 1]:
                curr += 1
            else:
                longest = max(curr, longest)
                curr = 1

        return max(curr, longest)

