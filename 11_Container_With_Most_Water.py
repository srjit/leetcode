
from typing import List

class Solution:

    def maxArea(self, height: List[int]) -> int:

        i, j = 0, len(height)-1
        max_area = 0
        while i < j:
            
            min_height = min(height[i], height[j])
            breadth = j - i
            area = breadth * min_height
            max_area = area if area > max_area else max_area

            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_area
        
        

s = Solution()        
height = [1,1]
print(s.maxArea(height))
