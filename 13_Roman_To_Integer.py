
class Solution:

    def romanToInt(self, s: str) -> int:

        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000   
        }

             
        prev = values[s[0]]
        res = prev
        for ch in s[1:]:
            current = values[ch]
            if current > prev:
                res -= prev
                current -= prev

            res += current            
            prev = current
        return res-

s = Solution()
print(s.romanToInt("MCMXCV"))

