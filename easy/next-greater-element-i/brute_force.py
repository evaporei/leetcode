class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        n_to_idx = {}
        for i, n in enumerate(nums1):
            n_to_idx[n] = i
        
        for i in range(len(nums2)):
            if nums2[i] not in n_to_idx:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    res[n_to_idx[nums2[i]]] = nums2[j]
                    break
        
        return res

