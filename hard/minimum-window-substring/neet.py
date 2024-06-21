class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return t
        
        count_t, window = Counter(t), Counter()
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float('inf')

        left = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1

            if ch in count_t and window[ch] == count_t[ch]:
                have += 1
            
            while have == need:
                window_size = right - left + 1
                if window_size < res_len:
                    res = [left, right]
                    res_len = window_size

                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1
        [l, r] = res
        return s[l:r+1] if res_len < float('inf') else ''
