class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        dp1, dp2 = 2, 1
        for stairs_left in range(3, n + 1):
            dp1 += dp2
            dp2 = dp1 - dp2
        
        return dp1