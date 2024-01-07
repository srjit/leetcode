class Solution:

    def isPalindrome(self, x: int) -> bool:

        s = str(x)
        r = len(s) - 1
        mid = int(r/2) + 1
        
        for i in range(mid):
            if s[i] != s[r]:
                return False
            r-=1
        return True


s = Solution()
print(s.isPalindrome(121))