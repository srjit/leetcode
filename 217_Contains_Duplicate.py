
class Solution:

    def containsDuplicate(self, nums) -> bool:

        _d = {}
        for num in nums:
            if num not in _d:
                _d[num] = 0
            _d[num] += 1
            if _d[num] >= 1:
                return True
        return False
        
        

s = Solution()
print(s.containsDuplicate([1,2,3,4]))