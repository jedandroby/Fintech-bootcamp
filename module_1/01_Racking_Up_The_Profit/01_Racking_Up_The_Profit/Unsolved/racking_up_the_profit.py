"""Racking up the profit."""

# Suppose each stock price is the same
stock_price = 30

# But that dividend yields vary across five stocks in your portfolio
dividend_yields = [0.035, 0.040, 0.072, 0.012, 0.052]

# @TODO: Create a variable to hold tallied dividend income
# YOUR CODE HERE!
total_dividend_income = 0


# @TODO: Create a for loop to calculated and add up all the dividend income
# YOUR CODE HERE!
for x in dividend_yields:
    dividend_income = x * stock_price 
    total_dividend_income = total_dividend_income + dividend_income

    print(f'Your dividend yield will be: ${dividend_income}')

# @TODO: Once it's all done, print the dividend income for the entire portfolio
# YOUR CODE HERE!
print(f'Your total dividend yield will be:${total_dividend_income}!')
