from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {c: [] for c in range(numCourses)}
        indorder = {c: 0 for c in graph}
        for a, b in prerequisites:
            graph[b].append(a)
            indorder[a] += 1
        
        q = deque([c for c in indorder if indorder[c] == 0])
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for nei in graph[course]:
                indorder[nei] -= 1
                if indorder[nei] == 0:
                    q.append(nei)
        
        if len(res) != numCourses:
            return []

        return res