from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = max(profit, prices[sell]-prices[buy])
            else:
                buy = sell
            sell += 1
        return profit

    def maxProfit_0(self, prices: List[int]) -> int:
        lowest_price_seen = 101
        max_profit = 0
        for price in prices:
            profit_today = max(price - lowest_price_seen, 0) # money we make if we sell today
            if profit_today > max_profit:
                max_profit = profit_today
            if price < lowest_price_seen:
                lowest_price_seen = price
        return max_profit
        
            


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit([5,1,5,6,7,1,10]) == 9
    assert solution.maxProfit([10,1,5,6,7,1]) == 6
    assert solution.maxProfit([10,8,7,5,2]) == 0
    print("All test cases passed!")