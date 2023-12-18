
class Solution:

    def reverse(self, x: int) -> int:

        is_negative = False
        if x < 0:
            is_negative = True
        
        reversed = int(str(abs(x))[::-1])
        import ipdb
        if reversed > 2**31 - 1 or reversed < -2**31:
            #ipdb.set_trace()
            return 0
        else:
            if is_negative:
                reversed = -reversed
        #ipdb.set_trace()
        return reversed


s = Solution()
s.reverse(1534236469)        


        