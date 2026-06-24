class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if sum([(num - 1) // mid + 1 for num in piles]) <= h:
                r = mid
            else:
                l = mid + 1
        return l

        # def yum(speed):
        #     return sum([(pile - 1) // speed + 1 for pile in piles]) <= h
        
        # left, right = 1, max(piles)
        # while left < right:
        #     mid = left + (right - left) // 2
        #     if yum(mid):
        #         right = mid
        #     else:
        #         left = mid + 1
        
        # return left