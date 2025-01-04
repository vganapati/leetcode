from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def maxProfit_0(i, have_coin):
            if i >= len(prices):
                return 0
            
            if (i, have_coin) in memo:
                return memo[(i, have_coin)]
            
            if have_coin:
                sell = maxProfit_0(i+2, not(have_coin)) + prices[i]
                cooldown = maxProfit_0(i+1, have_coin)
                memo[(i, have_coin)] = max(sell, cooldown)
            else:
                buy = maxProfit_0(i+1, not(have_coin)) - prices[i]
                cooldown = maxProfit_0(i+1, have_coin)
                memo[(i, have_coin)] = max(buy, cooldown)
            return memo[(i, have_coin)]

        return maxProfit_0(0,False)
    
solution = Solution()

prices = [1,2,3,0,2]
assert solution.maxProfit(prices) == 3

prices = [1]
assert solution.maxProfit(prices) == 0