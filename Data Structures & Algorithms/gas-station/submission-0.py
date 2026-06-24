class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if n == 1:
            return 0 if gas[0] >= cost[0] else -1

        s, l = 0, 1
        cur = gas[s] - cost[s]
        while s != l:
            if cur < 0:
                s = (s - 1) % n
                cur += gas[s] - cost[s]
            else:
                cur += gas[l] - cost[l]
                l = (l + 1) % n
        
        return s if cur >= 0 else -1
        
