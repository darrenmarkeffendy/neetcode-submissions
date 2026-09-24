class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        returned_list = []
        for word in strs:
            count = [0] * 26
            for character in word:
                count[ord(character)- ord('a')] += 1
            dictionary[tuple(count)].append(word)
        return list(dictionary.values())

        
        
       
