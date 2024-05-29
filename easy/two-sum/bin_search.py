class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ns = list(sorted([(n, i) for i, n in enumerate(nums)]))
        low = 0
        high = len(nums) - 1

        while low < high:
            s = ns[low][0] + ns[high][0]
            if s == target:
                return [ns[low][1], ns[high][1]]
            elif s > target:
                high -= 1
            else:
                low += 1
