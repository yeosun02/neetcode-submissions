class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, comb, tot):
            if tot == target:
                res.append(comb.copy())
                return
            if i >= len(candidates) or tot > target:
                return
            
            comb.append(candidates[i])
            dfs(i, comb, tot + candidates[i])
            comb.pop()
            dfs(i + 1, comb, tot)
        
        dfs(0, [], 0)
        return res
