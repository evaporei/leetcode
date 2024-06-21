class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        left = 0
        for right in range(len(s2)):
            while right - left + 1 > len(s1):
                left += 1
            if Counter(s2[left:right+1]) == s1_count:
                return True
        
        return False

