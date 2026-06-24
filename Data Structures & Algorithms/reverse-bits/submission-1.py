class Solution:
    def reverseBits(self, n: int) -> int:
        # binn = bin(n)[:1:-1]
        # return int(binn + "0" * (32 - len(binn)), 2)
        res = 0
        for i in range(32):
            if n & 1:
                res |= 1 << (31 - i)
            n >>= 1
        
        return res