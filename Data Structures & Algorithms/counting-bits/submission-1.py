class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        cnt = 1
        for i in range(1, n + 1):
            if i & i - 1 == 0:
                ans[i] = 1
                cnt *= 2
            else:
                ans[i] = 1 + ans[i - cnt//2]
        
        return ans