from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1]*(amount+1)
        memo[0] = 0

        for i in range(1,amount+1):
            options = []
            for coin in coins:
                if (i-coin) >= 0:
                    if memo[i-coin] != -1:
                        options.append(memo[i-coin]+1)
            if len(options)>0:
                memo[i] = min(options)
            else:
                memo[i] = -1

        return memo[amount]

solution = Solution()

coins = [1,2,5]; amount = 11
assert solution.coinChange(coins, amount) == 3

coins = [2]; amount = 3
assert solution.coinChange(coins, amount) == -1

coins = [1]; amount = 0
assert solution.coinChange(coins, amount) == 0