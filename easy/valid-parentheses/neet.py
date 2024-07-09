parens = {
    ')': '(',
    ']': '[',
    '}': '{'
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch not in parens:
                # opening
                stack.append(ch)
            else:
                if stack and stack[-1] == parens[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
