class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        counter = 0
        while counter < len(s):
            position = counter
            while s[position] != '#':
                position += 1
            length = int(s[counter : position])
            end = position + 1 + length
            start = position + 1
            decoded_strs.append(s[start: end])
            counter = end
        return decoded_strs
