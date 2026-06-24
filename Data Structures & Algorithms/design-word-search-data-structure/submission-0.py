class WordNode:
    def __init__(self):
        self.letters = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.letters:
                node.letters[char] = WordNode()
            node = node.letters[char]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.end

            if word[i] == ".":
                for child in node.letters.values():
                    if dfs(child, i + 1):
                        return True
                return False
            
            if word[i] not in node.letters:
                return False
            
            return dfs(node.letters[word[i]], i + 1)
        
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)