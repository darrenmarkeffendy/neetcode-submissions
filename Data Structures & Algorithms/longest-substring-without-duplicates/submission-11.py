class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set = set()
        counter = 0
        max_value = 0
        string = ''
        for i in s:
            if i in string:
                parts = string.split(f'{i}', 1)
                string = parts[1] + i
                counter = len(string)
            else:
                string += i
                counter += 1
            max_value = max(counter, max_value)
        return max_value
        