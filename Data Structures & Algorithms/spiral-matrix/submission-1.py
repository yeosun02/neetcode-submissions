class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        tot = m * n
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        it = 0
        res = []
        k = n
        i = 0
        j = -1
        for x in range(tot):
            i += dir[it % 4][0]
            j += dir[it % 4][1]
            res.append(matrix[i][j])
            k -= 1
            if not k:
                it += 1
                m -= 1 if it & 1 else 0
                n -= 1 if not it & 1 else 0
                k = [n, m][it & 1]
        
        return res