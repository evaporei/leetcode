class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for ch in s:
                chars[ord(ch) - ord('a')] += 1
            counts[tuple(chars)].append(s)
        return counts.values()
