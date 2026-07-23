class Solution:
    def myPow(self, x: float, n: int) -> float:
        base = x
        sign = 1 if n >= 0 else -1
        n = abs(n)
        res = 1
        while n:
            if n & 1:
                res *= base
            
            base *= base
            n >>= 1
        
        return res if sign == 1 else 1/res