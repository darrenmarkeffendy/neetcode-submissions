class Solution:
    def findMin(self, nums: List[int]) -> int:

        while nums:

            left = 0
            right = len(nums) - 1
            mid = (left+right) // 2

            if nums[mid] < nums[right]:
                nums = nums[:mid + 1]

            elif nums[mid] > nums[right]:
                nums = nums[mid + 1:]

            elif nums[mid] == nums[right]:
                return nums[mid]