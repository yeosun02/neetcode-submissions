class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()

        for word in words:
            root = trie
            for c in word:
                if c not in root.children:
                    root.children[c] = TrieNode()
                root = root.children[c]
                
            root.end = True        
        # q = deque([trie])
        # while q:
        #     qlen = len(q)
        #     p = []
        #     for i in range(qlen):
        #         node = q.popleft()
        #         for c in node.children:
        #             q.append(node.children[c])
        #             p.append([c, node.children[c].end])
            
        #     print(p)

        
        m = len(board)
        n = len(board[0])
        res = set()
        def dfs(i, j, node, word):
            if i < 0 or i == m or j < 0 or j == n or board[i][j] not in node.children:
                return False
            
            char = board[i][j]
            if node.children[char].end:
                res.add(word + char)

            board[i][j] = ""
            up = dfs(i - 1, j, node.children[char], word + char)
            down = dfs(i + 1, j, node.children[char], word + char)
            left = dfs(i, j - 1, node.children[char], word + char)
            right = dfs(i, j + 1, node.children[char], word + char)
            board[i][j] = char
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")
        
        return list(res)