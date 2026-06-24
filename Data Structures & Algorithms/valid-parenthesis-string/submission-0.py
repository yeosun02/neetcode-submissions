class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, ch in enumerate(s):
            if ch == "(":
                left.append(i)
            elif ch == "*":
                star.append(i)
            elif left:
                left.pop()
            elif star:
                star.pop()
            else:
                return False
        
        while left:
            if not star or left.pop() > star.pop():
                return False
        
        return True