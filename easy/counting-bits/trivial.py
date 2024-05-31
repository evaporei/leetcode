class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = hamming_weight(i)
        return res

def hamming_weight(n: int) -> int:
    weight = 0
    for i in range(32):
        weight += (n >> i) & 1
    return weight
