class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(int)
        for ch in s:
            counter[ch] += 1
        length = 0
        odd = False
        for v in counter.values():
            if v % 2 == 0:
                length += v
            else:
                odd = True
                length += v - 1
        return length + 1 if odd else length
