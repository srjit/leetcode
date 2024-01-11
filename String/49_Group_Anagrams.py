from collections import Counter
from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        _d = {}

        for _str in strs:

            s = "".join(sorted(_str))
            if s not in _d:
                _d[s] = []
            _d[s].append(_str)

        op = []
        for k, v in _d.items():
            op.append(v)
        return op



print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

        

        