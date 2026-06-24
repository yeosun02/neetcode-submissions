class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            cnt = {}
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in cnt:
                    return False
                
                cnt[board[row][col]] = 1
        
        for col in range(9):
            cnt = {}
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in cnt:
                    return False
                
                cnt[board[row][col]] = 1
        
        def check_box(r, c):
            cnt = {}
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    print(i, j, cnt, board[i][j])
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in cnt:
                        return False
                    cnt[board[i][j]] = 1
            
            return True

        for i in range(9):
            if not check_box(i % 3 * 3, i // 3 * 3):
                return False
        
        return True