class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += st + "ㅏ"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        prev = 0
        for i in range(len(s)):
            if s[i] == "ㅏ":
                res.append(s[prev:i])
                prev = i + 1
        return res