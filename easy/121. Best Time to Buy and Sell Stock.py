prices = [7,6,4,3,1]
buy = prices[0]
profit = 0
for i in prices:
    if i <= buy:
        buy = i
    elif i > buy:
        if i - buy > profit:
            profit = i - buy