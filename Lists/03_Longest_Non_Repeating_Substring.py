class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars = set()
        l = 0
        maxlen = 0
        for r in range(len(s)):

            while s[r] in chars:
                chars.remove(s[l])
                l+=1

            chars.add(s[r])
            maxlen = max(maxlen, r-l+1)

        return maxlen