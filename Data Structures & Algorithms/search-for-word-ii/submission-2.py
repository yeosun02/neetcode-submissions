class Trie:
    def __init__(self, val=None):
        self.children = {}
        self.is_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        words_T = Trie()
        res = set()

        for word in words:
            cur = words_T
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Trie()
                
                cur = cur.children[c]
            
            cur.is_word = True
        
        def dfs(r, c, string, node, visited):
            visited.add((r, c))
            string += board[r][c]
            if node.is_word:
                res.add(string)

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if ((nr, nc) not in visited
                    and 0 <= nr < m and 0 <= nc < n 
                    and board[nr][nc] in node.children):
                    dfs(nr, nc, string, node.children[board[nr][nc]], visited)
            
            visited.remove((r, c))
        
        for r in range(m):
            for c in range(n):
                if board[r][c] in words_T.children:
                    dfs(r, c, "", words_T.children[board[r][c]], set())
            
        return list(res)