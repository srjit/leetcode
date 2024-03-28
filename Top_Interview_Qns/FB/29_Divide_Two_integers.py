

class Solution:

    def sign(self, n1, n2):
        if (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
            return 1
        else:
            return -1




    def divide(self, dividend: int, divisor: int) -> int:
        
        mult = self.sign(dividend, divisor)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = mult * len(range(divisor, dividend+1, divisor))

        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        result = min(max(result, minus_limit), plus_limit)

        return result


print(Solution().divide(7, -3))
