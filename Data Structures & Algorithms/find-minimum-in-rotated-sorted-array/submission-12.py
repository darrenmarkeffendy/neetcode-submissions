class Solution:
    def findMin(self, nums: List[int]) -> int:
        least = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                least = min(least, nums[left])
                break

            mid = (left+right) // 2
            least = min(nums[mid], least)

            if nums[mid] < nums[right]:
                right = mid

            else:
                left = mid + 1

        return least