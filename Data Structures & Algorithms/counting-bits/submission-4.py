class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        p = 1

        for i in range(1, n + 1):
            if i == 2 * p:
                p <<= 1
            
            res[i] = 1 + res[i - p]
        
        return res