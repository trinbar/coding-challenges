# Given a list called stock_prices, where:

# The indices are the time (in minutes) past trade opening time, which was 
#  9:30am local time.
# The values are the price (in US dollars) of one share of Apple stock at that time.
# So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

#Write an efficient function that takes stock_prices and returns the best profit
#  I could have made from one purchase and one sale of one share of Apple stock yesterday.

#For example:

  #stock_prices = [10, 7, 5, 8, 11, 9]

 #get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

#Gotchas:
#No "shorting"—you need to buy before you can sell.
#Also, you can't buy and sell in the same time step—at least 1 minute has to pass.
  # Can't just return the max minus min because highest price might come
    # before lowest price. Must buy before sell.
    # return max(stock_prices) - min(stock_prices)

#If price goes down all day, best profit will be negative

def get_max_profit(stock_prices):
    """Returns the max profit of stock prices in a list.
        eg. stock_prices = [9, 11, 8, 5, 7, 10]
           returns 5
    """

    #ValueError if no more than 1 stock price
    if len(stock_prices) < 2:
        raise ValueError("Determining profit requires a minumum of two prices")

    #Initialize a max and a min profit
    minimum_price = stock_prices[0]
    maximum_profit = stock_prices[1] - stock_prices[0]

    for current_time in range(1,len(stock_prices)):
        current_price = stock_prices[current_time]

        potential_profit = current_price - minimum_price

        maximum_profit = max(maximum_profit, potential_profit)

        minimum_price = min(minimum_price, current_price)

    return maximum_profit

  

    
