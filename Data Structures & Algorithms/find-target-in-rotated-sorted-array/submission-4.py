class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle
        

            elif target > nums[middle]:
                if target > nums[right] and nums[middle] < nums[left]:
                    right = middle - 1
                else:
                    left = middle + 1

            else:
                if target < nums[left] and nums[middle] > nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1


