
from typing import List

class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        if n > 0:
            j = 0
            for i in range(m+n):
                if j < n and nums2[j] <= nums1[i]:
                        nums1.insert(i, nums2[j])                
                        j+=1 
                    
            
           
            i=j+m
            while j < n:
                nums1.insert(i, nums2[j])
                i+=1
                j+=1

        
        for _ in range(n):
            nums1.pop()
        print(nums1)
        


nums1 = [2,0]
m=1
nums2 = [1]
n=1
s = Solution()
print(s.merge(nums1, m, nums2, n))