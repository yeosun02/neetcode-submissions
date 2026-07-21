class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def first_diff_char(word1, word2):
            idx = 0
            while idx < len(word1) and idx < len(word2) and word1[idx] == word2[idx]:
                idx += 1
            
            if idx < len(word1) and idx < len(word2):
                return idx
            
            if idx == len(word2) and idx < len(word1):
                return -2

            return -1

        edges = {}
        in_degrees = {}
        chars = set(words[0])
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            chars |= set(word2)
            idx = first_diff_char(word1, word2)
            if idx == -1:
                continue
            elif idx == -2:
                return ""
            
            if word1[idx] not in edges:
                edges[word1[idx]] = []
            
            if word2[idx] not in edges[word1[idx]]:
                edges[word1[idx]].append(word2[idx])
                in_degrees[word2[idx]] = 1 + in_degrees.get(word2[idx], 0)
        
        queue = deque([char for char in chars if char not in in_degrees])
        res = ""
        while queue:
            char = queue.popleft()
            res += char
            if char not in edges:
                continue

            for nei in edges[char]:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 0:
                    queue.append(nei)
        
        print(chars, res)
        if len(res) < len(chars):
            return ""
        
        return res