


class Solution:

    def longestPalindrome(self, s: str) -> str:

        dp = [[0 for j in range (len(s)+1)] for i in range(len(s)+1)]
        
        for i in range(len(s)-1, -1, -1):            
            for j in range(i, -1, -1):                
                tmp = 0
                if s[i] == s[j]:
                    tmp+=1
                    if dp[i+1][j] == 1:
                        tmp += 1
                
                dp[i][j] = tmp  

        import ipdb
        ipdb.set_trace()

        maxlen = 0
        for dig_id in range(len(s)):
            tmp = 0
            

            for k in range(dig_id-1, 0, -1):
                tmp += dp[dig_id+1][k]
            
            if tmp > 0:
                dp[dig_id][dig_id] = 2*tmp + 1
            if maxlen < dp[dig_id][dig_id]:
                maxlen = dp[dig_id][dig_id]

        import ipdb
        ipdb.set_trace()

        return maxlen


print(Solution().longestPalindrome("ababbd"))