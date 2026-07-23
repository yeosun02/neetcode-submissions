class DSU:
    def __init__(self, n):
        self.comps = n
        self.size = [1] * (n + 1)
        self.parents = [i for i in range(n + 1)]
    
    def find(self, u):
        pu = self.parents[u]
        if pu != u:
            return self.find(pu)
        
        return pu
    
    def connect(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        
        if self.size[pu] > self.size[pv]:
            pu, pv = pv, pu
        
        self.size[pv] += self.size[pu]
        self.parents[pu] = pv
        return True
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        for a, b in edges:
            if not dsu.connect(a, b):
                return [a, b]
        