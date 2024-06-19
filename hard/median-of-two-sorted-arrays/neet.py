class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        left, right = 0, len(nums1) - 1

        while True:
            i = (left + right) // 2
            j = half - i - 2

            left1 = nums1[i] if i >= 0 else float("-inf")
            right1 = nums1[i+1] if (i + 1) < len(nums1) else float("inf")
            left2 = nums2[j] if j >= 0 else float("-inf")
            right2 = nums2[j+1] if (j + 1) < len(nums2) else float("inf")

            # partition is correct
            if left1 <= right2 and left2 <= right1:
                # odd
                if total % 2:
                    return min(right1, right2)
                # even
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1

