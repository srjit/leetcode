class Solution:

    def convertToBase7(self, num: int) -> str:

        if num == 0:
            return "0"

        tmp = abs(num)
        rem = 0
        res = ""


        while tmp != 0:
            rem = tmp % 7
            tmp = tmp // 7
            res += str(rem)
            
        res = res[::-1] if num >= 0 else "-" + res[::-1]
        return res


print(Solution().convertToBase7(0))

        