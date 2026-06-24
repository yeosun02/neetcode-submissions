class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        return a if a < max_int else ~(a ^ mask)
        # c = res = 0
        # for i in range(32):
        #     res |= ((a & 1) ^ (b & 1) ^ c) << i
        #     c = (a & b & 1) | (a & c) | (b & c)
        #     a >>= 1
        #     b >>= 1
        
        # return ~(res ^ (2**32 - 1)) if res >= 0x7FFFFFFF else res