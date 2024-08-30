digitToLetters = {
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r','s'],
    '8': ['t','u', 'v'],
    '9': ['w','x','y','z'],
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        def backtrack(i: int, combination: str):
            if len(combination) == len(digits):
                res.append(combination)
                return
            for ch in digitToLetters[digits[i]]:
                backtrack(i + 1, combination + ch)
        if digits:
            backtrack(0, '')
        return res
