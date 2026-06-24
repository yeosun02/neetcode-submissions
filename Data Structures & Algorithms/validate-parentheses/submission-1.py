class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_b = {'(': ')', '[': ']', '{': '}'}
        for bracket in s:
            if bracket in open_b:
                stack.append(bracket)
            else:
                if not stack or open_b[stack.pop()] != bracket:
                    return False
        
        return not stack
                