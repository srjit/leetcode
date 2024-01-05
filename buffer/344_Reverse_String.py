from typing import List

class Solution:

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s) // 2
        for i in range(mid+1):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        return s
        
print(Solution().reverseString(['h', 'e', 'l', 'l', 'o', 'w']))