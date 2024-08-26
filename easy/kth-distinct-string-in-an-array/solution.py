class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        stack = []

        for s in arr:
            if counts[s] == 1:
                stack.append(s)
        
        return stack[k-1] if k <= len(stack) else ""
