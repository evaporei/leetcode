class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort() # to skip duplicates

        def backtrack(i: int, subset: List[int]):
            if i >= len(nums):
                subsets.append(subset)
                return
            backtrack(i + 1, subset + [nums[i]])
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return subsets
