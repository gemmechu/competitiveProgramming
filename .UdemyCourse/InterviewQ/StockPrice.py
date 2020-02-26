def profit(prices : list):
    if(len(prices) < 2):
        return
    max_profit = prices[1] - prices[0]
    min_stock = prices[0]

    for stock in (prices[1:]):

        compare = stock - min_stock
        max_profit = max(max_profit, compare)
        min_stock = min(min_stock, stock)
    return max_profit

prices =[5,3,1]
print(profit(prices))