m = [
    [1000, 'M'],
    [900, 'CM'],
    [500, 'D'],
    [400, 'CD'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10, 'X'],
    [9, 'IX'],
    [5, 'V'],
    [4, 'IV'],
    [1, 'I']
]

class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        
        for minus, s in m:
            if num >= minus:
                count = num // minus
                res += (s * count)
                num = num % minus

        return res
