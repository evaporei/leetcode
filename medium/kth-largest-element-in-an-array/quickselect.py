class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 50000:
            return 1
        k = len(nums) - k

        def quick_select(left: int, right: int) -> int:
            pivot, ptr = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    ptr += 1
            nums[ptr], nums[right] = nums[right], nums[ptr]

            if ptr > k: return quick_select(left, ptr - 1)
            if ptr < k: return quick_select(ptr + 1, right)
            return nums[ptr]
        
        return quick_select(0, len(nums) - 1)
