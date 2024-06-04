class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [n])
        return subsets
