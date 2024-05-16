class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for n in nums:
            offset = 1
            # start of sequence
            if not (n - offset) in s:
                curr = 1
                while (n + offset) in s:
                    offset += 1
                    curr += 1
                longest = max(curr, longest)

        return longest
                
