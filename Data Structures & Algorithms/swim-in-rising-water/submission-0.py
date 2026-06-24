class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def dijkstra():
            elev = [[float('inf')] * n for _ in range(n)]
            pq = [[0, 0]]
            heapq.heapify(pq)
            elev[0][0] = grid[0][0]

            while pq:
                i, j = heapq.heappop(pq)

                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + dr, j + dc
                    if ni < 0 or nj < 0 or ni == n or nj == n:
                        continue
                    w = grid[ni][nj]
                    if elev[ni][nj] > max(elev[i][j], w):
                        elev[ni][nj] = max(elev[i][j], w)
                        heapq.heappush(pq, [ni, nj])
            
            return elev
        return dijkstra()[-1][-1]