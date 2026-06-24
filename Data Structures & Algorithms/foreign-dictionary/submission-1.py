class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for w in words for c in w}
        prev = words[0]
        for word in words[1:]:
            i = 0
            while i < len(prev) and i < len(word) and prev[i] == word[i]:
                i += 1
            
            if i < len(prev) and i >= len(word):
                return ""

            if i < len(prev) and i < len(word):
                graph[prev[i]].add(word[i])
            
            prev = word
        
        visited = {}
        res = []
        def dfs(node):
            if node in visited:
                return visited[node]
            
            visited[node] = True
            for nei in graph[node]:
                if dfs(nei):
                    return True
            
            visited[node] = False
            res.append(node)
            return False
        
        for char in graph:
            if dfs(char):
                return ""
        
        res.reverse()
        return "".join(res)