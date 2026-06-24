class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for r in range(n // 2):
            for c in range(r, n - r - 1):
                temp = matrix[r][c]
                matrix[r][c] = matrix[-c - 1][r]
                matrix[-c - 1][r] = matrix[-r - 1][-c - 1]
                matrix[-r - 1][-c - 1] = matrix[c][-r - 1]
                matrix[c][-r - 1] = temp
            