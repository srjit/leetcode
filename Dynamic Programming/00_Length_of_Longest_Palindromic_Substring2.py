class Solution:

    def longestPalindrome(self, s: str) -> str:
        
        _len = len(s)
        dp = [[0 for j in range(_len)] for i in range(_len)]

        for k in range(_len):
            dp[k][k] = 1
        
        for j in range(_len):
            for i in range(_len):
                if i < j:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]+2
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i+1][j])
            

        maxlen = dp[0][_len - 1]

        import ipdb
        ipdb.set_trace()

        return maxlen


print(Solution().longestPalindrome("cbbd"))



