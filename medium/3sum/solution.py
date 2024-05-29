class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            low = i + 1
            high = len(nums) - 1
            while low < high:
                s = n + nums[low] + nums[high]
                if s > 0:
                    high -= 1
                elif s < 0:
                    low += 1
                else:
                    res.append([n, nums[low], nums[high]])
                    low += 1
                    while nums[low] == nums[low - 1] and low < high:
                        low += 1

        return res
