class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posi = sorted([(pos, i) for i, pos in enumerate(position)], reverse=True)
        fleets = []
        for pos, i in posi:
            if not fleets:
                fleets.append((pos, (target - pos) / speed[i]))
                continue
            
            if (target - pos) / speed[i] > fleets[-1][1]:
                fleets.append((pos, (target - pos) / speed[i]))
        
        return len(fleets)