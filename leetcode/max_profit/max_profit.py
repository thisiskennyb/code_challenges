def max_profit(prices):
    max_profit = 0

    left = 0
    right = 1

    while right < len(prices):
        if prices[right] < prices[left]:
            left = right
            right +=1
        elif prices[right] - prices[left] > max_profit:
            max_profit = prices[right] - prices[left]
            right += 1
        else:
            right += 1

    return max_profit
         



price_list = [7,1,5,3,6,4]
print(max_profit(price_list))