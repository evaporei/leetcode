from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for s in strs:
            c = frozenset(Counter(s).items())
            l = counts.get(c, [])
            l.append(s)
            counts[c] = l
        return counts.values()
