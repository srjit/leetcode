
def longest_palindromic_substring(s):

    n = len(s)
    if n == 1:
        return s
    dp = [[False] * n for _ in range(n)]# 2D array of n x n with all values set to False
    longest_palindrome = ""
    
    # single characters are palindromes
    for i in range(n):
        dp[i][i] = True
        longest_palindrome = s[i]

    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
    
