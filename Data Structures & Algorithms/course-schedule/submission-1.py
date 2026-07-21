class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = {i:0 for i in range(numCourses)}
        edges = {i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            edges[a].append(b)
            in_degrees[b] += 1
        
        order = []
        q = deque([course for course in range(numCourses) if in_degrees[course] == 0])
        while q:
            course = q.popleft()
            order.append(course)
            for nei in edges[course]:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 0:
                    q.append(nei)
        
        if len(order) < numCourses:
            return False
        
        return True