from collections import defaultdict
from typing import List


class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        negatives = {}
        positives = {}
        zeros = 0
        for num in nums:
            if num < 0:
                negatives[num] += 1
            elif num > 0:
                positives[num] += 1
            else:
                zeros += 1

        result = []
        if zeros:
            for n in negatives:
                if -n in positives:
                    result.append((0, -n, n))       
            if zeros > 2:
                result.append((0,0,0))

        return result, positives, negatives
        

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))       