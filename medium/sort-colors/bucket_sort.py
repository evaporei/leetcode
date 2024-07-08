class Solution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = [0, 0, 0]
        for color in nums:
            buckets[color] += 1
        
        offset = 0
        for color in range(len(buckets)):
            n = buckets[color]
            for i in range(offset, offset + n):
                nums[i] = color
                offset += 1
            
