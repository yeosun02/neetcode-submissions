class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        works = {}
        for task in tasks:
            works[task] = 1 + works.get(task, 0)
        
        works = [-cnt for cnt in works.values()]
        heapq.heapify(works)

        res = 0
        while len(works):
            cntr = []
            interval = min(len(works), n + 1)
            for _ in range(interval):
                cnt = -heapq.heappop(works)
                cntr.append(cnt)
            res += n + 1
            for cnt in cntr:
                if cnt - 1 == 0:
                    continue
                heapq.heappush(works, -cnt + 1)
            
            if len(works) == 0:
                res -= n + 1 - interval
        
        return res