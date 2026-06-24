class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        tank = 0
        res = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                res = i + 1
        
        return res
        # n = len(gas)
        # if n == 1:
        #     return 0 if gas[0] >= cost[0] else -1

        # s, l = 0, 1
        # cur = gas[s] - cost[s]
        # while s != l:
        #     if cur < 0:
        #         s = (s - 1) % n
        #         cur += gas[s] - cost[s]
        #     else:
        #         cur += gas[l] - cost[l]
        #         l = (l + 1) % n
        
        # return s if cur >= 0 else -1
        
