def maxProfit(prices):
    max_profit=0
    for ind, p in enumerate(prices):
        profit = max(prices[ind:])-p
        if profit>max_profit:
            max_profit=profit
    return max_profit

def maxProfit_efficient(prices):
    max_profit=-10000
    min_value = 10000
    max_value = max(prices)
    for ind, p in enumerate(prices):
        if p < min_value:
            min_value = p
            profit = max_value - min_value
            if profit>max_profit:
                max_profit=profit
        if p == max_value and ind < len(prices)-1:
            max_value = max(prices[ind+1:])
            min_future_val = min(prices[ind+1:])
            if max_value <= min_future_val:
                # print(max_value)
                # print(min_value)
                break
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
print(maxProfit_efficient(prices))