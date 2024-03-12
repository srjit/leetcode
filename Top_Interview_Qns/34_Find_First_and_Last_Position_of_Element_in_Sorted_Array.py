
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l, r = 0, len(nums)-1

        first, last  = -1, -1
        while l <= r:

            m = (l + r)//2
            if nums[m] == target:
                first = m
                break

            elif nums[m] < target:
                l = m + 1
            
            elif nums[m] > target:
                r = m - 1

        if first == -1:
            return [-1, -1]
        else:
            
            import ipdb
            ipdb.set_trace()
        



print(Solution().searchRange([8,8,8,8,8,10], 8))        