class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        starting_position = 0
        last_seen = {}
        counter = 0
        max_value = 0
        string = ''
        for position, character in enumerate(s):
            if character in last_seen:
                if last_seen[character] >= starting_position:
                    starting_position = last_seen[character] + 1
            last_seen[character] = position
            window_length = position - starting_position + 1
            max_value = max(window_length, max_value)
        return max_value
        