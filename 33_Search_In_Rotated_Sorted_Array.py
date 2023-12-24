from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # target is not here - it is in the unsorted right part
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # target is in the unsorted left part
                    right = mid - 1

        return -1


print(Solution().search([2,5,8,9,13,15], 15))
