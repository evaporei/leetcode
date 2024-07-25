class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        
        k = len(nums)
        for n, count in m.items():
            while count > 1:
                nums.remove(n)
                k -= 1
                count -= 1
        
        return k
