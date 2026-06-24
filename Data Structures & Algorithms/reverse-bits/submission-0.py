class Solution:
    def reverseBits(self, n: int) -> int:
        binn = bin(n)[:1:-1]
        return int(binn + "0" * (32 - len(binn)), 2)