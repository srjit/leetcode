
from typing import List

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]] :

        result = []

        if (len(nums) == 1):
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            
            # permute the other elements
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)

            # 
            nums.append(n)

        return result


s = Solution()
print(s.permute([1,2,3]))
                
                 