

class Solution:

    def isPowerOfThree(self, n: int) -> bool:

        if n < 0:
            return False
        elif n==1:
            return True
        else:

            n = abs(n)

            mul = 1
            while mul <= n:
                
                mul *= 3
                if mul == n:
                    return True
            return False
           

        

print(Solution().isPowerOfThree(-3))