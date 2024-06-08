class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        stack = [] # idxs
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                idx = stack.pop()
                answers[idx] = i - idx
            stack.append(i)
        return answers
