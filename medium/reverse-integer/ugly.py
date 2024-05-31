MAX_INT32 = 2**31

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            s = str(x)
            i = int(s[::-1])
            return i if i <= MAX_INT32 else 0
        s = str(x)[1:]
        i = -int(s[::-1])
        return i if i >= -MAX_INT32 else 0
