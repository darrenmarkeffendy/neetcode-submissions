class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        starts = set()
        consecutive= set()
        for number in num_set:
            if number - 1 not in num_set:
                starts.add(number)
        
        for number in starts:
            counter = 1
            while number + 1 in num_set:
                counter += 1
                number += 1
            consecutive.add(counter)

        return max(consecutive, default=0)
