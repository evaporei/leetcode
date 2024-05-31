MAX = 2**31
MIN = -MAX

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        while x:
            res *= 10
            digit = int(math.fmod(x, 10)) # can't be % ;-;
            res += digit
            x = int(x / 10) # can't be // ;-;
        if res >= MAX or res <= MIN:
            return 0
        return res
