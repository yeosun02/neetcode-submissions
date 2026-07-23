class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = {i: 0 for i in range(numCourses)}
        edges = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            edges[b].append(a)
            in_degrees[a] += 1
        
        q = deque([node for node in in_degrees if in_degrees[node] == 0])
        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for nei in edges[node]:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == numCourses else []