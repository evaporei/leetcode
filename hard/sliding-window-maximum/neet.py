class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deque = collections.deque() # indexes
        left = right = 0

        while right < len(nums):
            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()
            deque.append(right)
             
            if left > deque[0]:
                deque.popleft()
            
            if (right + 1) >= k:
                res.append(nums[deque[0]])
                left += 1
            
            right += 1

        return res
