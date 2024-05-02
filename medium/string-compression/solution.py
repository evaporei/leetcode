class Solution:
    def compress(self, s: List[str]) -> int:
        old_len = len(s)
    
        index = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            s[index] = s[i]
            index += 1
            count = j - i
            if count > 1:
                for ch in str(count):
                    s[index] = ch
                    index += 1
            i = j
    
        if old_len > index:
            del s[index:]
            return index
    
        return old_len

