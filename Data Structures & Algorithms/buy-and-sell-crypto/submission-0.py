class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # everytime the price is lower reset
        # loop, if the item is greater than keep going otherwise reset the start node 

        # profit = trade open - max value reached
        # Loop through all of numbers in prices
        # if current is less than the previous
        # calculate the profit for that trade 
        # reset the trade open and keep going until end of the lsit

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
        
        return max_profit


                