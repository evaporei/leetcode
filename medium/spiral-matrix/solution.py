class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(m[0])
        top, bottom = 0, len(m)
        
        while left < right and top < bottom:
            for j in range(left, right):
                res.append(m[top][j])
            top += 1

            for i in range(top, bottom):
                res.append(m[i][right - 1])
            right -= 1

            # # eg: 1 row or 1 col matrix
            # if not (left < right and top < bottom):
            if len(res) == len(m) * len(m[0]):
                break
            
            for j in reversed(range(left, right)):
                res.append(m[bottom - 1][j])
            bottom -= 1

            for i in reversed(range(top, bottom)):
                res.append(m[i][left])
            left += 1

        return res

