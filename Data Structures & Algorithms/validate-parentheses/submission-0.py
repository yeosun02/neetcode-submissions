class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_b = {'(': 0, '[': 1, '{': 2}
        close_b = [')', ']', '}']
        for bracket in s:
            if bracket in open_b:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                
                if close_b[open_b[stack.pop()]] != bracket:
                    return False
        
        return not stack
                