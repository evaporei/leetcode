class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = deque((ch.lower() for ch in s if ch.isalnum()))

        while d:
            left = d.popleft()
            try:
                right = d.pop()
            except IndexError:
                continue
            if left != right:
                return False
        
        return True
