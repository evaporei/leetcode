class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        
        ptr1, ptr2 = nums[0], slow
        while ptr1 != ptr2:
            ptr1, ptr2 = nums[ptr1], nums[ptr2]
            
        return ptr1
