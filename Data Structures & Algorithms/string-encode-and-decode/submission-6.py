class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string = encoded_string + string + "Blind_75" 
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split("Blind_75")
        return decoded_strs[:-1]
