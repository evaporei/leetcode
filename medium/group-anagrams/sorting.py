class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for s in strs:
            ss = str(sorted(s))
            l = counts.get(ss, [])
            l.append(s)
            counts[ss] = l
        return counts.values()
