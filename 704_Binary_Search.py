from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        _left, _right = 0, len(nums)

        while _left < _right:
            _mid = (_left + _right) // 2 

            if nums[_mid] == target:
                # Check if _mid is the first occurrence of the target
                while _mid > 0 and nums[_mid - 1] == target:
                    _mid -= 1
                return _mid
            elif nums[_mid] < target:
                _left = _mid + 1
            else:
                _right = _mid

        return -1


print(Solution().search([-3,-2,-1,0,0, 0, 0, 0,1,2], 0))        


            
        