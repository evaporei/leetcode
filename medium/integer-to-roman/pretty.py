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
        res = []
        
        while num:
            for minus, s in m:
                if num >= minus:
                    res.append(s)
                    num -= minus
                    break
            else:
                continue

        return ''.join(res)
