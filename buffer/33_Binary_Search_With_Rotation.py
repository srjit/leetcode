from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)
        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # left is ordered
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # target is not present in the ordered left
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1






print(Solution().search([4,5,6,7,0,1,2], 2))