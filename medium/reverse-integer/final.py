MIN = -2**31 # -2bi ending in 8
MAX = -MIN - 1 # 2bi ending in 7

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        while x:
            digit = int(math.fmod(x, 10)) # can't be % ;-;
            x = int(x / 10) # can't be // ;-;
            if will_overflow(res, digit):
                return 0
            res *= 10
            res += digit
        return res

def will_overflow(res: int, digit: int) -> bool:
    return (res > MAX // 10 or
            (res == MAX // 10 and digit >= MAX % 10) or
            res < MIN // 10 or
            (res == MIN // 10 and digit <= MIN % 10))
