class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = -1
        s_diff = 0
        need = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            need += diff
            if start == -1:
                if diff >= 0:
                    start = i
                    s_diff = need - diff
            elif need < s_diff:
                start = -1
        
        return start if need >= 0 else -1
                