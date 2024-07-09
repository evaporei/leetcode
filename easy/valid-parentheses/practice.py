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
                if stack:
                    op = stack.pop()
                    if op != parens[ch]:
                        return False
                else:
                    return False
        return len(stack) == 0
