class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = int(str(abs(x))[::-1])

        if (sign == 1 and x > 2**31 - 1) or (sign == -1 and x > 2**31):
            return 0
        
        return x if sign == 1 else -x
        