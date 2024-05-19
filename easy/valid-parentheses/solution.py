class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if stack:
                    last = stack.pop()
                    if ((last == '(' and ch != ')') or
                        (last == '[' and ch != ']') or
                        (last == '{' and ch != '}')):
                        return False
                else:
                    return False
        return len(stack) == 0
