class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums) - 1, -1, -1):
            cur = []
            for subs in res:
                cur.append(subs + [nums[i]])
            res += cur
        
        return res