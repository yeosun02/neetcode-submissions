class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1 # gets the least significant bit
            res += 1
        
        return res
        # res = 0
        # while n0:
        #     res += n & 1
        #     n >>= 1
        
        # return res