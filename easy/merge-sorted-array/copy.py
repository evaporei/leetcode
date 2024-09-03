class Solution:
    def merge(self, res: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1 = res.copy()
        i = j = k = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res[k] = nums1[i]
                i += 1
            else:
                res[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            res[k] = nums1[i]
            i += 1
            k += 1
        while j < n:
            res[k] = nums2[j]
            j += 1
            k += 1
