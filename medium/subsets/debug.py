def subsets(nums: list[int]) -> list[list[int]]:
    res = []

    def backtrack(i: int, subset: list[int]):
        breakpoint()
        if i >= len(nums):
            res.append(subset)
            return
        
        backtrack(i + 1, subset + [nums[i]])
        backtrack(i + 1, subset)

    backtrack(0, [])
    return res

subsets([1, 2, 3])
