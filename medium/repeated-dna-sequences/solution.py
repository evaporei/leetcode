class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dnas = defaultdict(int)
        left, right = 0, 9
        while right < len(s):
            dnas[s[left:right+1]] += 1
            left += 1
            right += 1

        res = []
        for window, count in dnas.items():
            if count > 1:
                res.append(window)
        
        return res
