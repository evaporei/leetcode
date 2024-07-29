class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idxs = []
        for i, n in enumerate(nums):
            if n == 0:
                idxs.append(i)
        
        for idx in reversed(idxs):
            del nums[idx]
        
        for _ in idxs:
            nums.append(0)
