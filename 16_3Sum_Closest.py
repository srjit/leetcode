
from typing import List

class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)
        _difference = float('inf')
        result = 0
        for i in range(len(nums)):

            start = i+1
            end = len(nums)-1
            while start < end:
                _sum = nums[i] + nums[start] + nums[end]
                if _sum == target:
                    return target
                elif abs(target - _sum) < _difference:
                    _difference = abs(target - _sum)
                    result = _sum                
                if _sum < target:
                    start += 1
                else:
                    end -=1
                    
        return result

        
        

                


            


        