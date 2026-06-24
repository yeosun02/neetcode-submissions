class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)

        def find(i, j, idx):
            if idx == w:
                return True

            if i < 0 or j < 0 or i == m or j == n or word[idx] != board[i][j]:
                return False
            
            orig_letter = board[i][j]
            board[i][j] = ''
            res = (find(i + 1, j, idx + 1) or 
                find(i - 1, j, idx + 1) or
                find(i, j + 1, idx + 1) or
                find(i, j - 1, idx + 1))
            board[i][j] = orig_letter
            return res
        
        for i in range(m):
            for j in range(n):
                if find(i, j, 0):
                    return True
        
        return False