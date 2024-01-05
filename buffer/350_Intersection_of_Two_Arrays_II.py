from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        _c1 = dict(Counter(nums1))
        _c2 = dict(Counter(nums2))


        res = []
        for k, v in _c1.items():
            if k in _c2:

                _count = min(_c1[k], _c2[k])
                res += [k] * _count
        
        

        return res


print(Solution().intersect([1,2,2,1], [2,2]))