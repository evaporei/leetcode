class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = nums[:n]
        right = nums[n:]
        j = k = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = left[j]
                j += 1
            else:
                nums[i] = right[k]
                k += 1
        
        return nums
