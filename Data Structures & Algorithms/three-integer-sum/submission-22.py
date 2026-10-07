class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_list = []
        nums.sort()
        for i in range(len(nums)):
            if i >=1 and nums[i] == nums[i-1]:
                continue
            left_pointer, right_pointer = i+1, len(nums) - 1
            while left_pointer < right_pointer:
                two_sum = nums[left_pointer] + nums[right_pointer]
                if two_sum + nums[i] == 0:
                    return_list.append([nums[left_pointer], nums[right_pointer], nums[i]])
                    left_pointer += 1
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer-1]:
                        left_pointer += 1
                elif two_sum + nums[i] < 0:
                    left_pointer += 1
                elif two_sum + nums[i] > 0:
                    right_pointer -= 1
        return return_list


