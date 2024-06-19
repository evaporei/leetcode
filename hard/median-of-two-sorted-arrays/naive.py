class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()

        even = len(nums3) % 2 == 0
        if even:
            mid1 = (len(nums3) - 1) // 2
            mid2 = mid1 + 1
            return (nums3[mid1] + nums3[mid2]) / 2
        mid = (len(nums3) - 1) // 2
        return nums3[mid]
