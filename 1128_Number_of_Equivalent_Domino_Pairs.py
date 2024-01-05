
from typing import List
from math import comb

class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        _dominos = {}

        for [d1, d2] in dominoes:
            if d1 > d2:
                d1, d2 = d2, d1
            if (d1,d2) not in _dominos:
                _dominos[(d1,d2)] = 0
            _dominos[(d1,d2)]+=1

        # import ipdb
        # ipdb.set_trace()

        return sum([comb(v,2) for k,v in _dominos.items() if v>1])


print(Solution().numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2], [2,2]]))            