from typing import List

class Solution:

        def coinChange(self, coins: List[int], amount: int) -> int:

            dp = [amount+1] * (amount+1)

            dp[0] = 0
            for amt in range(amount+1):
                for c in range(len(coins)):
                    dp[amt] = min(dp[amt], 1+(amt-c))

            return dp[amount] if dp[amount] != amount+1 else -1

