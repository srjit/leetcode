
from typing import List

class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {} # (index, sum uptill now)

        def backtrack(i: int, total: int):

            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            # one for addition and one for subtraction
            dp[(i, total)] = backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i])
            return dp[(i, total)]

        return backtrack(0,0)



print(Solution().findTargetSumWays([1,1,1,1,1], 3))