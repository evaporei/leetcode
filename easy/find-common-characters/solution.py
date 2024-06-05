class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words
        res = []
        for ch in set(words[0]):
            frequency = min((word.count(ch) for word in words))
            res += [ch] * frequency
        return res
