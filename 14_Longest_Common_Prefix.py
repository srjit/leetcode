
class Solution:

    def longestCommonPrefix(self, strs):

        ans=""
        # sort the elements in the array
        v=sorted(strs)
        first=v[0]
        last=v[-1]

        # First element will be most different prefix of all
        # comparisons
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

        

        

s = Solution()
print(s.longestCommonPrefix( ["preheat","oven","prehistoric"]))