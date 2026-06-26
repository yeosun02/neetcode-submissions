class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            frequency = [0] * 26
            for char in word:
                frequency[ord(char) - ord('a')] += 1
            
            frequency = tuple(frequency)
            if frequency not in anagrams:
                anagrams[frequency] = []
            
            anagrams[frequency].append(word)
        
        return list(anagrams.values())