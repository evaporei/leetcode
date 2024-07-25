class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Encode the new values in the higher bits of each element
        for i in range(n):
            nums[i] |= (nums[i + n] << 10)  # Assuming all elements are < 1024
        
        # Decode the new values back into the array
        j = 2 * n - 1
        for i in reversed(range(n)):
            nums[j] = nums[i] >> 10  # New value from higher bits
            nums[j - 1] = nums[i] & 1023  # Original value
            j -= 2
        
        return nums
