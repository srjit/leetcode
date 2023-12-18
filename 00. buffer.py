#
#
#  Integer to Roman
#
#

from typing import List

class Solution:

    def convert_to_parts(self, rem: int) -> List:

        op = []
        start = 1000
        while start > 0:
            quo = rem // start
            rem = rem % start
            op.append(quo * start)
            start = start // 10
            
        if rem != 0:
            op.append(rem)

        return op
        

    def intToRoman(self, num: int) -> str:

        parts = self.convert_to_parts(num)

        roman_d = {
               1: 'I',
               4: 'IV',
               5: 'V',
               9: 'IX',
              10: 'X',
              40: 'XL',
              50: 'L',
              90: 'XC',
             100: 'C',
             400: 'CD',
             500: 'D',
             900: 'CM',
            1000: 'M'
        }
        breaks = [4, 9, 39, 89, 400, 900]

        op_str = ""

        import ipdb
        ipdb.set_trace()
        for part in parts:
            closest = breaks[0]
            for b in breaks:
                if part >= b:
                    break
                closest = b
            

s = Solution()
print(s.intToRoman(2481))

# -------------------------------------------------------------------------  #