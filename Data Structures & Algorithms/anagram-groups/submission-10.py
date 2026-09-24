class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        returned_list = []
        for i in strs:
            dictionary[''.join(sorted(i))].append(i)
       
        for index in dictionary:
            returned_list.append(dictionary[index])
        return returned_list

        
        
       
