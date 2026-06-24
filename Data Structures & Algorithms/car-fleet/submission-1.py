class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s_pos = sorted([(position[i], speed[i]) for i in range(len(speed))], reverse=True)

        res = [0]
        for p, s in s_pos:
            t = (target - p) / s
            if res[-1] < t:
                res.append(t)
        
        return len(res) - 1