class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        tmp = 1
        for i in range(len(nums)):
            pref[i] = tmp
            tmp *= nums[i]
        post = [1] * len(nums)
        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] *= tmp
            tmp *= nums[i]
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pref[i] * post[i]
        return res

