import ipdb

class Solution:

    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        else:
            _n = int(n/2)
            _tmp = self.myPow(x, _n)
            res =  _tmp * _tmp

            if n%2 != 0:
                if n < 0:
                    res *= 1/x
                else:
                    res *= x
            return res
        

print(Solution().myPow(3, -3))        