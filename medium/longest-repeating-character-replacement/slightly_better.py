class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        longest = 0
        max_count = 0
        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            max_count = max(max_count, count[idx])
            window = right - left + 1
            replacements = window - max_count
            if replacements <= k:
                longest = max(longest, window)
            else:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
        return longest

