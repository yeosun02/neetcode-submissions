import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = [[] for _ in range(n)]
        for start, dst, weight in edges:
            adj_list[start].append((weight, dst))

        dist = {}
        queue = [(0, src)]
        while queue:
            weight, dst = heapq.heappop(queue)
            if dst in dist:
                continue
            
            dist[dst] = weight
            for w, d in adj_list[dst]:
                if d not in dist:
                    heapq.heappush(queue, (w + weight, d))
        
            
        for i in range(n):
            if i not in dist:
                dist[i] = -1
    
        return dist