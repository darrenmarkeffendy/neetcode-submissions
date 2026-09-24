class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        returned_list = []
        dictionary = defaultdict(int)
        for number in nums:
            dictionary[number] += 1
        for _ in range(k):
            topkFrequent = max(dictionary, key=dictionary.get)
            returned_list.append(topkFrequent)
            dictionary.pop(topkFrequent)
        return returned_list