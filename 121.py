def maxProfit(prices):
    max_profit=0
    for ind, p in enumerate(prices):
        profit = max(prices[ind:])-p
        if profit>max_profit:
            max_profit=profit
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))