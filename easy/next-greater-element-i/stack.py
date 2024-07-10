class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        n_to_idx = {}
        for i, n in enumerate(nums1):
            n_to_idx[n] = i
        
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = n_to_idx[val]
                res[idx] = curr
            if curr in n_to_idx:
                stack.append(curr)
        
        return res

