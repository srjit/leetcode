
from typing import List
class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:


        if len(nums) == 0:
            return 0
        else:
            longest_length = 1
            mid = len(nums) // 2
            i, j = mid-1, mid+1
            pivot_l, pivot_r = nums[mid], nums[mid]
        
            while i >= 0 :
                if nums[i] < pivot_l:
                    
                    longest_length += 1
                    pivot_l = nums[i]
                i-=1
            while j < len(nums):
                if nums[j] > pivot_r:
                    longest_length += 1
                    pivot_r = nums[j]
                j+=1

        return longest_length


s = Solution()
print(s.lengthOfLIS([0,1,0,3,2,3]))