class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        dp[""] = True
        def helper(s):
            if s in dp:
                return dp[s]
            
            dp[s] = False
            for word in wordDict:
                if s[:len(word)] == word:
                    dp[s] |= helper(s[len(word):])
            
            return dp[s]
        
        return helper(s)
        # @cache
        # def helper(s):
        #     if s == "":
        #         return True
            
        #     for word in wordDict:
        #         if s[:len(word)] == word and helper(s[len(word):]):
        #             return True
            
        #     return False
        
        # return helper(s)