
class Solution:

    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n != 0 and n != 1:
            rem = n % 2
            weight += rem
            n = n // 2
        if n == 1:
            weight += n
        
        return weight
        



s = Solution()
print(s.hammingWeight(0b11111111111111111111111111111101))
        