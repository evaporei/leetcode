class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i: int, combination: List[int], total: int):
            if total == target:
                res.append(combination)
                return
            if total > target or i >= len(candidates):
                return
            dfs(i, combination + [candidates[i]], total + candidates[i])
            dfs(i + 1, combination, total)
        dfs(0, [], 0)
        return res
            
