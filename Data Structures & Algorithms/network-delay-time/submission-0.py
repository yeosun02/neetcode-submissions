class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        times = {k: 0}
        pq = [(0, k)]
        heapq.heapify(pq)
        while pq:
            cur_t, cur_node = heapq.heappop(pq)
            if cur_t > times.get(cur_node, cur_t):
                continue
            
            for nei, t in graph[cur_node]:
                new_t = t + cur_t
                if new_t < times.get(nei, new_t + 1):
                    times[nei] = new_t
                    heapq.heappush(pq, (new_t, nei))
        
        return -1 if len(times) < n else max(times.values())