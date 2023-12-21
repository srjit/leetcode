
from typing import List

class Solution:

    def kSumClosest(self, nums: List[int], target: int, k: int) -> int:

        nums = sorted(nums)

        if k == 2:
            i, j = 0, len(nums)-1
            diff = float('inf')
            result = None
            while i < j:
                _sum  = nums[i] + nums[j]
                _diff = abs(target - _sum)
                if _sum == target:
                    return _sum
                elif _sum <= target:
                    i+=1
                else:
                    j-=1
                
                if _diff < diff:
                    diff = _diff
                    result = _sum
            return result

        else:

            result = None
            diff = float('inf')
            for i in range(len(nums)):
                import ipdb
                next_level_closest = self.kSumClosest(nums[i+1:], target-nums[i], k-1)
                ipdb.set_trace()
                _sum = nums[i] + next_level_closest
                
                _diff = abs(target - _sum)

                if _diff < diff:
                    diff = _diff
                    result = _sum
            return result







s = Solution()
print(s.kSumClosest([-1,2,1,-4], 1, 3))





            
            

            
        
