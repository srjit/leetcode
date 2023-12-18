
class Solution:

    def reverse(self, x: int) -> int:

        is_negative = False
        if x < 0:
            is_negative = True
        
        reversed = int(str(abs(x))[::-1])
        if reversed > 2**31 - 1 or reversed < -2**31:
            return 0
        else:
            if is_negative:
                reversed = -reversed
        return reversed


s = Solution()
s.reverse(1534236469)        


        