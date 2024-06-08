class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            for j in range(i + 1, len(temperatures)):
                if temperature < temperatures[j]:
                    answers[i] = j - i
                    break
        return answers
