
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        current_max, current_min = 1, 1
        maxproduct = nums[0]

        for i in range(len(nums)):

            
            products = (nums[i], current_max*nums[i], current_min*nums[i])
            current_max, current_min = max(products), min(products)
            maxproduct = max(maxproduct, current_max)
        


        return maxproduct

print(Solution().maxProduct([-2,0,-1]))