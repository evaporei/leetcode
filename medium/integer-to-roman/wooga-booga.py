class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        
        while num:
            s = ''
            minus = 0
            if num >= 1000:
                s = 'M'
                minus = 1000
            elif num >= 900:
                s = 'CM'
                minus = 900
            elif num >= 500:
                s = 'D'
                minus = 500
            elif num >= 400:
                s = 'CD'
                minus = 400
            elif num >= 100:
                s = 'C'
                minus = 100
            elif num >= 90:
                s = 'XC'
                minus = 90
            elif num >= 50:
                s = 'L'
                minus = 50
            elif num >= 40:
                s = 'XL'
                minus = 40
            elif num >= 10:
                s = 'X'
                minus = 10
            elif num >= 9:
                s = 'IX'
                minus = 9
            elif num >= 5:
                s = 'V'
                minus = 5
            elif num >= 4:
                s = 'IV'
                minus = 4
            else:
                s = 'I'
                minus = 1
            res.append(s)
            num -= minus

        return ''.join(res)
