class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not x or n == 1:
            return x
        if n == 0:
            return 1

        nn = abs(n)
        res = 1
        while nn:
            if nn & 1:
                res *= x
            x *= x
            nn >>= 1
        
        return res if n > 0 else 1/res
        # return x**n