class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = my_bisect_right(nums, -1)
        pos = len(nums) - my_bisect_left(nums, 1)
        return max(neg, pos)

# [-2, -1, -1, 1, 2, 3], -1
# [-2, -1, -1] are smaller or equal to -1
# return 3
def my_bisect_right(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low

# [-2, -1, -1, 1, 2, 3], 1
# [1, 2, 3] are bigger than or equal to 1
# return 3 (ptr to first element >= target)
def my_bisect_left(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low
