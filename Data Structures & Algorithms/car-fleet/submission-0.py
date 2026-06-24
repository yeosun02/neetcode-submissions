class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s_pos = sorted([(position[i], speed[i]) for i in range(len(speed))], reverse=True)

        res = [(target - s_pos[0][0])/s_pos[0][1]]
        for p, s in s_pos[1:]:
            t = (target - p) / s
            if res[-1] < t:
                res.append(t)
        
        return len(res)