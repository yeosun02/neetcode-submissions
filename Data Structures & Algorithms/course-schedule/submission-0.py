class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, preq in prerequisites:
            graph[preq].append(course)
        visited = [0 for _ in range(numCourses)]

        def dfs(root):
            if visited[root] == -1:
                return False
            if visited[root] == 1:
                return True

            visited[root] = -1
            res = True
            for node in graph[root]:
                res &= dfs(node)
            visited[root] = 1 if res else -1
            return res
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True