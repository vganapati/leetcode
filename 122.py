def maxProfit(prices):
    profit = 0
    for ind in range(len(prices)-1):
        profit_i = prices[ind+1]-prices[ind]
        if profit_i>0:
            profit += profit_i
    return profit


prices = [7,1,5,3,6,4]
assert maxProfit(prices)==7