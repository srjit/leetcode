# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version >= 4:
        return True
    return False

class Solution:

    def firstBadVersion(self, n: int) -> int:

        l, r = 1, n

        while l < r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        
        return l

print(Solution().firstBadVersion(5))
        
            