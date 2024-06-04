class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i: int, subset: List[int]):
            if i >= len(nums):
                res.append(subset)
                return
            
            backtrack(i + 1, subset + [nums[i]])
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
