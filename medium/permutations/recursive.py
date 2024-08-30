class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i: int, options: List[int], curr: List[int]):
            if i >= len(nums):
                res.append(curr)
                return
            for n in options:
                new_options = options.copy()
                new_options.remove(n)
                dfs(i+1, new_options, curr + [n])
        dfs(0, nums, [])
        return res
