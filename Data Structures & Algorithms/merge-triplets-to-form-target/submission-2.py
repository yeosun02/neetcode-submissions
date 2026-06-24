class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            x |= a == target[0]
            y |= b == target[1]
            z |= c == target[2]
            if x and y and z:
                return True
        
        return False