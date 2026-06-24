class Solution:
    def reverseBits(self, n: int) -> int:
        # binn = bin(n)[:1:-1]
        # return int(binn + "0" * (32 - len(binn)), 2)
        res = 0
        for i in range(32):
            res |= (n >> i & 1) << (31 - i)
        
        return res