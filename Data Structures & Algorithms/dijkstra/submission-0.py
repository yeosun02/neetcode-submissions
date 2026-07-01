import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        dist = {i:float("inf") for i in range(n)}
        adj_list = [[] for _ in range(n)]
        for start, dst, weight in edges:
            adj_list[start].append((weight, dst))

        queue = [(0, src)]
        while queue:
            weight, dst = heapq.heappop(queue)
            if dist[dst] < weight:
                continue
            
            dist[dst] = weight
            for w, d in adj_list[dst]:
                heapq.heappush(queue, (w + weight, d))
        
            
        for k, v in dist.items():
            if v == float("inf"):
                dist[k] = -1
    
        return dist