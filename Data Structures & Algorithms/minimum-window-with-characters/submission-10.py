class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_characters = defaultdict(int)
        s_characters = defaultdict(int)
        string = ''
        best_string = ''

        for letter in t:
            t_characters[letter] += 1

        for right in range(len(s)):
            string += s[right]
            if s[right] in t_characters:
                s_characters[s[right]] += 1
                if all(s_characters[i] >= t_characters[i] for i in t_characters):
                    
                    while string[0] not in t_characters or s_characters[string[0]] > t_characters[string[0]]:
                        s_characters[string[0]] -= 1
                        string = string[1:]

                    if len(string) <= len(best_string) or not best_string:
                        best_string = string

            if not s_characters:
                string = string[1:]


        if not best_string:
            return ''
        else:
            return best_string