class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_string = "".join(char for char in s if char.isalnum()).lower()
        print(formatted_string)
        for i in range(len(formatted_string)):
            if formatted_string[i] != formatted_string[-i-1]:
                return False
        return True
        