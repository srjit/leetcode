from typing import List

class Solution:

    def one_digit_addition(self, a, b, carry):

        a, b, c = int(a), int(b), int(carry)
        sum = a + b + c

        d_ = {0: (0, 0), 
            1: (1, 0),
            2: (0, 1),
            3: (1, 1)}
        
        return d_[sum]

    def add_one(self, prev: List) -> int :

        # binary is always kept as reversed list
        binary = []
        carry = 0
        count_of_ones = 0
        operand = [1] + ([0] * (len(prev) - 1))
        
        for _x, _y in zip(prev, operand):
            sum, carry = self.one_digit_addition(_x, _y, carry)
            count_of_ones += sum
            binary.append(sum)

        if carry == 1:
            binary.append(carry)
            count_of_ones += 1

        return binary, count_of_ones


    def countBits(self, n: int) -> List[int]:

        result = [0]

        binary_of_prev = [0]
        for num in range(1, n+1):
            binary_of_prev, count_of_ones = self.add_one(binary_of_prev)
            result.append(count_of_ones)

        return result
            


s = Solution()
print(s.countBits(2))
        