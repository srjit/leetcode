from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1

        import ipdb
        ipdb.set_trace()
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))