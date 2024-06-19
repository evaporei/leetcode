class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1
            seen_chars.add(s[right])
            max_len = max(max_len, right - left + 1)
            
        return max_len

