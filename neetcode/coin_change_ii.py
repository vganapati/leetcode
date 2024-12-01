from typing import List
from collections import defaultdict

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        coins.sort()
        for ind, coin in enumerate(coins):
            if coin>amount:
                coins = coins[0:ind]
                break
        memo = [[-1]*(amount+1) for _ in range(len(coins))]
        def dfs(ind, amount):
            if memo[ind][amount] > -1:
                return memo[ind][amount]
            else:
                allowed_coins = coins[ind:]
                num_paths = 0
                for ind_1, coin in enumerate(allowed_coins):
                    if (amount - coin) == 0:
                        num_paths += 1
                    elif amount - coin > 0:
                        num_paths += dfs(ind+ind_1, amount-coin)
                    else:
                        num_paths += 0
                memo[ind][amount] = num_paths
            return num_paths

        output = dfs(0, amount)
        return output

solution = Solution()
amount = 4; coins = [3,2,1]
assert solution.change(amount, coins) == 4

amount = 7; coins = [2,4]
assert solution.change(amount, coins) == 0