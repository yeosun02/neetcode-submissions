class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        min_r = min_c = 0
        max_r = m - 1
        max_c = n - 1
        r = c = 0
        dr, dc = 0, 1
        while len(res) < m * n:
            res.append(matrix[r][c])
            if dc == 1 and c == max_c:
                min_r += 1
                dr, dc = 1, 0
            elif dc == -1 and c == min_c:
                max_r -= 1
                dr, dc = -1, 0
            elif dr == 1 and r == max_r:
                max_c -= 1
                dr, dc = 0, -1
            elif dr == -1 and r == min_r:
                min_c += 1
                dr, dc = 0, 1
            
            r += dr
            c += dc

        return res