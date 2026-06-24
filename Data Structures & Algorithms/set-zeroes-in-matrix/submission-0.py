class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rows, cols = set(), set()
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        
        # for i in rows:
        #     for j in range(n):
        #         matrix[i][j] = 0
        
        # for j in cols:
        #     for i in range(m):
        #         matrix[i][j] = 0
        
        m = len(matrix)
        n = len(matrix[0])
        top_fill = False
        for j in range(n):
            if matrix[0][j] == 0:
                top_fill = True

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        if top_fill:
            for j in range(n):
                matrix[0][j] = 0