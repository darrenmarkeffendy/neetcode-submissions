class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            if i != 0:
                prefix *= nums[i-1]
                output[i] = prefix
        for i in range(len(nums)):
            if i != 0:
                postfix *= nums[-i]
                output[-i-1] *= postfix
        return output




