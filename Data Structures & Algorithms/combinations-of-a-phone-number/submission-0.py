class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = [""]
        for digit in digits:
            cur = []
            for char in digit_to_letter[digit]:
                for comb in res:
                    cur.append(comb + char)
            
            res = cur
        
        return res