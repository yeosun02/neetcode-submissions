class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        buckets = [0] * (max(hand) + 1)
        for val in hand:
            buckets[val] += 1
        
        min_val = min(hand)
        for i in range(len(hand) // groupSize):
            cur = min_val
            for j in range(groupSize):
                if cur == len(buckets) or buckets[cur] == 0:
                    return False
                buckets[cur] -= 1
                cur += 1
            
            while min_val < len(buckets) and buckets[min_val] == 0:
                min_val += 1
        
        return True