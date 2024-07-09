class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for t in range(len(nums) - 2):
            # skip first element duplicates
            if t > 0 and nums[t] == nums[t-1]:
                continue

            l, r = t + 1, len(nums) - 1
            while l < r:
                target, left, right = nums[t], nums[l], nums[r]
                three_sum = target + left + right
                if three_sum == 0:
                    res.append([target, left, right])

                    # skip second element duplicates
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # skip third element duplicates
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1

        return res
                
