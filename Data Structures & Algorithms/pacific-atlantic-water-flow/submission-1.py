class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(r, c, val, ocean):
            if (r, c) in ocean or r < 0 or c < 0 or r == m or c == n or heights[r][c] < val:
                return
            
            ocean.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], ocean)

        # Pacific
        for r in range(m):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, n - 1, heights[r][n - 1], atlantic)
        for c in range(n):
            dfs(0, c, heights[0][c], pacific)
            dfs(m - 1, c, heights[m - 1][c], atlantic)
        
        res = []
        for loc in pacific:
            if loc in atlantic:
                res.append(loc)
        
        return res
        
        # m, n = len(heights), len(heights[0])
        # pacific = set()
        # atlantic = set()
        # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # def dfs(r, c, val, ocean):
        #     if (r, c) in ocean or r < 0 or c < 0 or r == m or c == n or heights[r][c] < val:
        #         return
            
        #     ocean.add((r, c))
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc, heights[r][c], ocean)

        # # Pacific
        # for r in range(m):
        #     pacific.add((r, 0))
        # for c in range(1, n):
        #     pacific.add((0, c))
        
        # for r in range(1, m):
        #     dfs(r, 1, heights[r][0], pacific)
        # for c in range(1, n):
        #     dfs(1, c, heights[0][c], pacific)

        # # Atlantic
        # for r in range(m):
        #     atlantic.add((r, n - 1))
        # for c in range(n - 1):
        #     atlantic.add((m - 1, c))

        # for r in range(m - 1):
        #     dfs(r, n - 2, heights[r][n - 1], atlantic)
        # for c in range(n - 1):
        #     dfs(m - 2, c, heights[m - 1][c], atlantic)
        
        # res = []
        # for loc in pacific:
        #     if loc in atlantic:
        #         res.append(loc)
        
        # return res