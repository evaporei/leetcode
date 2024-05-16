class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return aux(nums, target, 0, len(nums) - 1)

def aux(nums: List[int], target: int, low: int, high: int) -> int:
    if low <= high:
        mid = (high - low) // 2 + low
        if target > nums[mid]:
            return aux(nums, target, mid + 1, high)
        elif target < nums[mid]:
            return aux(nums, target, low, mid - 1)
        else:
            return mid
    else:
        return -1
