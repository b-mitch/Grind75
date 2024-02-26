'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

def best_day_to_buy_sell_stock(prices):
    # Track max possible profit with two pointers (buy & sell)
    max_profit, p1, p2 = 0, 0, 1
    while p2 < len(prices):
        # If sale price is lower than buy price, set buy pointer to sell pointer
        if prices[p2] < prices[p1]:
            p1 = p2
        # Otherwise, you have a net profit and should check if it's greater than current max profit
        else:
            profit = prices[p2] - prices[p1]
            max_profit = profit if profit > max_profit else max_profit
        p2 += 1
    return max_profit

# TESTS

print(best_day_to_buy_sell_stock([4,2,1,7]))
# >>5
print(best_day_to_buy_sell_stock([2,1]))
# >>2