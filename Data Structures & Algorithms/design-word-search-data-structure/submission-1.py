class Trie:
    def __init__(self):
        self.is_word = False
        self.children = {}
    
class WordDictionary:

    def __init__(self):
        self.words = Trie()

    def addWord(self, word: str) -> None:
        cur = self.words
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            
            cur = cur.children[char]
        
        cur.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            
            if word[i] == ".":
                for char in node.children:
                    if dfs(node.children[char], i + 1):
                        return True
                
                return False
            
            if word[i] not in node.children:
                return False
            
            return dfs(node.children[word[i]], i + 1)
        
        return dfs(self.words, 0)