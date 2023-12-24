
from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        arr = [nums[0]]
        maxSum = arr[0]
        for i in range(1, len(nums)):
            arr.append(max(arr[i-1]+nums[i], nums[i]))

            if maxSum < arr[i]:
                maxSum = arr[i]
            
        return maxSum

print(Solution().maxSubArray([5,4,-1,7,8]))