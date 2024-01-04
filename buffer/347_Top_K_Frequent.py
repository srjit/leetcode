import bisect 

from typing import List

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        _d = {}
        for num in nums:
            if num not in _d:
                _d[num] = 0
            _d[num] += 1
        
        frequencies = []
        for _,v in _d.items():
            bisect.insort(frequencies, v)
        
        gt_freq = frequencies[-k:][0]
        return list(set([k for k,v in _d.items() if v >= gt_freq]))
