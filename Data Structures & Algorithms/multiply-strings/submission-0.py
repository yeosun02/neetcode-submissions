class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (len(num1) < len(num2) 
            or (len(num1) == len(num2) and num1 < num2)):
            num1, num2 = num2, num1
        
        def to_int(digit: str) -> int:
            return ord(digit) - ord("0")

        res = 0
        for i in range(len(num2)):
            c = 0 
            cur = 0
            for j in range(len(num1)):
                digit = to_int(num2[-i - 1]) * to_int(num1[-j - 1]) + c
                c = digit // 10
                cur += (digit % 10) * 10 ** j
            
            cur += c * 10 ** (len(num1))
            res += cur * 10 ** i
        
        return str(res)