class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            word_len = len(word)
            encoded_string += str(word_len) + "$" + word
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        index = 0
        while index < len(s):
            word_len = 0
            while s[index] != "$":
                word_len = word_len * 10 + int(s[index])
                index += 1
            
            index += 1
            decoded_strs.append(s[index:index + word_len])
            index += word_len
        
        return decoded_strs
