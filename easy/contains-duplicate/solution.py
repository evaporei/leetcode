class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for n in nums:
            numsSet.add(n)
        return len(numsSet) != len(numsSet)
