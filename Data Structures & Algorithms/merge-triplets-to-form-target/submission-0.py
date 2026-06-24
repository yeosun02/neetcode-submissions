class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = False, False, False
        for a, b, c in triplets:
            x |= a == target[0] and b <= target[1] and c <= target[2]
            y |= a <= target[0] and b == target[1] and c <= target[2]
            z |= a <= target[0] and b <= target[1] and c == target[2]
        
        return x and y and z