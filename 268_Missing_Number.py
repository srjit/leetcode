from typing import List

class Solution:

    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        sum_observed = sum(nums)        
        sum_expected = (n*(n+1))/2

        return int(sum_expected - sum_observed)
         
        