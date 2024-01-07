class Solution:

    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        one, two = 1, 0
        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp

        return one

            
        
print(Solution().fib(3))        