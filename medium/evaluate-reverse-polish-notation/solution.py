class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if is_number(token):
                stack.append(int(token))
            else:
                res = 0
                op2 = stack.pop()
                op1 = stack.pop()
                if token == '+':
                    res = op1 + op2
                elif token == '/':
                    res = round(int(op1 / op2))
                elif token == '*':
                    res = op1 * op2
                else:
                    res = op1 - op2
                stack.append(res)
                
        return stack.pop()

def is_number(n: str) -> bool:
    try:
        int(n)
        return True
    except ValueError:
        return False
