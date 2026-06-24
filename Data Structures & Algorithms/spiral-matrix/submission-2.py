class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c, it = 0, -1, 0
        steps = [n, m - 1]
        while steps[it & 1]:
            for _ in range(steps[it & 1]):
                r += dir[it][0]
                c += dir[it][1]
                res.append(matrix[r][c])
            
            steps[it & 1] -= 1
            it += 1
            it %= 4
        
        return res