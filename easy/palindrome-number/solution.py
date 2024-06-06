class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        n = x
        while n:
            reverse *= 10
            remainder = n % 10
            reverse += remainder
            n //= 10
        return x == reverse
