class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        def dfs(i: int, curr: List[int], total: int):
            if total == target:
                combinations.append(curr)
                return
            if total > target or i >= len(candidates):
                return
            dfs(i + 1, curr + [candidates[i]], total + candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return combinations
