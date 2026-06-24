class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = [len(matrix[0]), len(matrix) - 1]
        
        r, c, it = 0, -1, 0
        while steps[it & 1]:
            for _ in range(steps[it & 1]):
                r += dir[it][0]
                c += dir[it][1]
                res.append(matrix[r][c])
            
            steps[it & 1] -= 1
            it += 1
            it %= 4
        
        return res

        # m = len(matrix)
        # n = len(matrix[0])
        # tot = m * n
        # dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # it = 0
        # res = []
        # k = n
        # i = 0
        # j = -1
        # for x in range(tot):
        #     i += dir[it % 4][0]
        #     j += dir[it % 4][1]
        #     res.append(matrix[i][j])
        #     k -= 1
        #     if not k:
        #         it += 1
        #         m -= 1 if it & 1 else 0
        #         n -= 1 if not it & 1 else 0
        #         k = [n, m][it & 1]
        
        # return res