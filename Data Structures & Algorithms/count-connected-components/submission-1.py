class DSU:
    def __init__(self, n: int) -> None:
        self.comp = n
        self.parents = [i for i in range(n)]
        self.size = [1] * n

    def find(self, n: int) -> int:
        if self.parents[n] != n:
            return self.find(self.parents[n])
        
        return self.parents[n]
    
    def update(self, u: int, v: int) -> None:
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return
        
        if self.size[pv] < self.size[pu]:
            pu, pv = pv, pu
        
        self.comp -= 1
        self.size[pv] += self.size[pu]
        self.parents[pu] = pv
    
    def components(self) -> int:
        return self.comp

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = DSU(n)
        for u, v in edges:
            nodes.update(u, v)
        
        return nodes.components()
         