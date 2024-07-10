import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    # floordiv doesn't work cause leetcode is bananas
    # and wants something specific
    '/': lambda a, b: round(int(a / b))
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                op = operations[token]
                b = stack.pop()
                a = stack.pop()
                stack.append(op(a, b))

        return stack[0]
