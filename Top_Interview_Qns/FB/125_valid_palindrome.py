import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alphabets = string.ascii_lowercase + string.digits
        s = "".join([x for x in s.lower().strip() if x in alphabets])

        print(s)
        ispal = True
        if len(s) > 1:
            for i in range((len(s)//2)+1):
                if s[i] != s[len(s)-i-1]:
                    ispal = False
                    break
        return ispal


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))        