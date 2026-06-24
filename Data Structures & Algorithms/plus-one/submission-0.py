class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        i = len(digits) - 1
        while i >= 0 and c:
            c, digits[i] = (digits[i] + c) // 10, (digits[i] + c) % 10
            i -= 1
        
        if c:
            return [1] + digits
        
        return digits