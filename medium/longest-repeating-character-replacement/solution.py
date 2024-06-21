class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        longest = 0
        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            window = right - left + 1
            replacements = window - max(count)
            if replacements <= k:
                longest = max(longest, window)
            else:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
        return longest

