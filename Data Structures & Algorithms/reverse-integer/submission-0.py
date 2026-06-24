class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            res *= 10
            res += x % 10
            x //= 10
        
        return res * sign if -MAX <= res < MAX else 0