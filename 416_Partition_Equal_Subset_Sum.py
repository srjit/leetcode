
from typing import List

class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        
        limit = len(nums)
        total = sum(nums)
        half = total / 2

        _set = {0}
        for i in range(limit-1, -1, -1):
            _buf = {x + nums[i] for x in _set}
            _set = _set.union(_buf)
            _set.add(nums[i])

        return half in _set



nums = [1,2,3,5]
print(Solution().canPartition(nums))

