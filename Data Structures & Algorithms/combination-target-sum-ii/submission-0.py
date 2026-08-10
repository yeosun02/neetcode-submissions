class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def dfs(idx, total, cur):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or idx == n:
                return
            
            cur.append(candidates[idx])
            dfs(idx + 1, total + candidates[idx], cur)
            cur.pop()

            while idx + 1 < n and candidates[idx] == candidates[idx + 1]:
                idx += 1
            
            dfs(idx + 1, total, cur)

        dfs(0, 0, [])
        return res