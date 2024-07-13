class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = [0] * (len(nums1) + len(nums2))
        k = i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged[k] = nums1[i]
                i += 1
            else:
                merged[k] = nums2[j]
                j += 1
            k += 1
        
        while i < len(nums1):
            merged[k] = nums1[i]
            i += 1
            k += 1
        
        while j < len(nums2):
            merged[k] = nums2[j]
            j += 1
            k += 1
        
        if len(merged) % 2 == 0:
            mid1 = (len(merged) - 1) // 2
            mid2 = mid1 + 1
            return (merged[mid1] + merged[mid2]) / 2
        mid = len(merged) // 2
        return float(merged[mid])
