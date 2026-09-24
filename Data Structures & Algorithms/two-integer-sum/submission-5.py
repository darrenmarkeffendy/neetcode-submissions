class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_list = []

        for index, num in enumerate(nums):
            complement = target - num

            if complement in nums and nums.index(complement) != index:
                return_list.append(index)
                return_list.append(nums.index(complement))
                return sorted(return_list)
