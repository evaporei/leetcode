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
                count_str = str(count)
                s[index:index + len(count_str)] = count_str
                index += len(count_str)
            i = j
    
        if old_len > index:
            del s[index:]
            return index
    
        return old_len

