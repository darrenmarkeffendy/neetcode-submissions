class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix  = 1
        prefix_array, suffix_array, output  = [], [], []
        for i in range(len(nums)):
            if i != 0:
                prefix *= nums[i-1]
                suffix *= nums[-i]
            prefix_array.append(prefix)
            suffix_array.append(suffix)

        suffix_array.reverse()
        for i in range(len(nums)):
            output.append(prefix_array[i] * suffix_array[i])
        return output



