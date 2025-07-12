class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                # update min price
                min_price = price 
            else:
                # selling
                max_profit = max(max_profit, price - min_price)  

        return max_profit
      
        """
         tips
        1. it's an orfered list, it could use two pointers to find the buying and selling
        2. the brute way is to iterate all the left and right elements
        3. so it's good to think how to decrease the steps
        4. if I know the lowest price, then I could decide which day to selling
        """
